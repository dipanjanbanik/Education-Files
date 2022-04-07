package failuredetector

import (
	"fmt"
	"time"
)

// EvtFailureDetector represents a Eventually Perfect Failure Detector as
// described at page 53 in:
// Christian Cachin, Rachid Guerraoui, and Luís Rodrigues: "Introduction to
// Reliable and Secure Distributed Programming" Springer, 2nd edition, 2011.
type EvtFailureDetector struct {
	id        int          // the id of this node
	nodeIDs   []int        // node ids for every node in cluster
	alive     map[int]bool // map of node ids considered alive
	suspected map[int]bool // map of node ids  considered suspected

	sr SuspectRestorer // Provided SuspectRestorer implementation

	delay         time.Duration // the current delay for the timeout procedure
	delta         time.Duration // the delta value to be used when increasing delay
	timeoutSignal *time.Ticker  // the timeout procedure ticker

	hbSend chan<- Heartbeat // channel for sending outgoing heartbeat messages
	hbIn   chan Heartbeat   // channel for receiving incoming heartbeat messages
	stop   chan struct{}    // channel for signaling a stop request to the main run loop

	testingHook func() // DO NOT REMOVE THIS LINE. A no-op when not testing.

	hbfrom     int
	hbto       int
	hbresponse bool
}

// NewEvtFailureDetector returns a new Eventual Failure Detector. It takes the
// following arguments:
//
// id: The id of the node running this instance of the failure detector.
//
// nodeIDs: A list of ids for every node in the cluster (including the node
// running this instance of the failure detector).
//
// ld: A leader detector implementing the SuspectRestorer interface.
//
// delta: The initial value for the timeout interval. Also the value to be used
// when increasing delay.
//
// hbSend: A send only channel used to send heartbeats to other nodes.
func NewEvtFailureDetector(id int, nodeIDs []int, sr SuspectRestorer, delta time.Duration, hbSend chan<- Heartbeat) *EvtFailureDetector {
	suspected := make(map[int]bool)
	alive := make(map[int]bool)

	// marking all the node as alive
	for x := range nodeIDs {
		alive[x] = true
	}

	return &EvtFailureDetector{
		id:        id,
		nodeIDs:   nodeIDs,
		alive:     alive,
		suspected: suspected,

		sr: sr,

		delay: delta,
		delta: delta,

		hbSend: hbSend,
		hbIn:   make(chan Heartbeat, 8),
		stop:   make(chan struct{}),

		testingHook: func() {}, // DO NOT REMOVE THIS LINE. A no-op when not testing.
	}
}

// Start starts e's main run loop as a separate goroutine. The main run loop
// handles incoming heartbeat requests and responses. The loop also trigger e's
// timeout procedure at an interval corresponding to e's internal delay
// duration variable.
func (e *EvtFailureDetector) Start() {
	e.timeoutSignal = time.NewTicker(e.delay)
	go func(timeout <-chan time.Time) {
		for {
			e.testingHook() // DO NOT REMOVE THIS LINE. A no-op when not testing.
			select {
			case <-e.hbIn:
				// delivering hearbeat reply
				if e.hbresponse {
					// if e.hbresponse == true {
					e.hbSend <- Heartbeat{
						From:    e.hbto,
						To:      e.hbfrom,
						Request: false,
					}
					// } else if e.hbresponse == false {
				} else if !e.hbresponse {
					e.alive[e.hbfrom] = true
				}
			case <-timeout:
				e.timeout()
			case <-e.stop:
				return
			}
		}
	}(e.timeoutSignal.C)
}

// DeliverHeartbeat delivers heartbeat hb to failure detector e.
func (e *EvtFailureDetector) DeliverHeartbeat(hb Heartbeat) {
	e.hbIn <- hb

	e.hbfrom = hb.From
	e.hbto = hb.To
	e.hbresponse = hb.Request
}

// Stop stops e's main run loop.
func (e *EvtFailureDetector) Stop() {
	e.stop <- struct{}{}
}

// Internal: timeout runs e's timeout procedure.
func (e *EvtFailureDetector) timeout() {
	tempSuspected := make(map[int]bool)

	// condition to check and increase delay
	// if any suspected value is found then the function will increase the delay
	for i := 0; i < len(e.alive)-1; i++ {
		if e.suspected[i] {
			e.delay = e.delay + e.delta
			break
		}
	}

	// populating tempSuspected when there is some value in e.suspected
	// if e.suspected is empty then tempSuspected value is nil
	if len(e.suspected) > 0 {
		for x, y := range e.suspected {
			tempSuspected[x] = y
		}
	} else {
		tempSuspected = nil
	}

	// function for passing the wantPostSuspected which will empty the
	// map of e.suspected
	emptySuspect := func() {
		for x := range e.suspected {
			delete(e.suspected, x)
		}
	}

	// condition to check the post suspect
	// if e.alive equals to the first e.nodeIDs then there is no post suspect
	// if e.alive is less then the e.nodeIDs then this will check which value
	// is missing from e.nodeIDs and mark as suspected(e.suspected[x] = true)
	if len(e.alive) == len(e.nodeIDs) {
		emptySuspect()
	} else if len(e.alive) < len(e.nodeIDs) {
		for x := range e.nodeIDs {
			// value, ok := e.alive[x]
			ok := e.alive[x]
			if ok {
				// fmt.Println("value: ", value)
				fmt.Println()
			} else {
				e.suspected[x] = true
			}
		}
	}

	// condition to check the alive and suspect status and set the restore or suspect value
	// here tempSuspected equals to e.suspected. tempSuspected introduced due to in
	// previous part we are calling emptySuspect() function which deletes the suspected
	// nodes.
	//if e.alive and tempSuspected have the empty(nil) map then it will initialize all the
	//e.nodeIDs as suspected
	// if e.alive is empty and tempSuspected is not empty it will do nothing
	// if e.alive is not empty and tempSuspected is empty it will do nothing
	// if e.alive and tempSuspected both are not empty it will check the suspected value
	// is present or not in e.alive. if it is found in e.alive then value will restore by
	// e.sr.Restore()
	if len(e.alive) == 0 && len(tempSuspected) == 0 {
		for i := 0; i < len(e.nodeIDs); i++ {
			e.sr.Suspect(e.nodeIDs[i])
		}
	} else if len(e.alive) == 0 && len(tempSuspected) != 0 {
		fmt.Println()
	} else if len(e.alive) != 0 && len(tempSuspected) == 0 {
		fmt.Println()
	} else if len(e.alive) != 0 && len(tempSuspected) != 0 {
		for x := range tempSuspected {
			// value, ok := e.alive[x]
			ok := e.alive[x]
			if ok {
				e.sr.Restore(x)
			} else {
				fmt.Println()
			}
		}
	}

	// sending heartbeat request
	for i := len(e.nodeIDs) - 1; i >= 0; i-- {
		e.hbSend <- Heartbeat{
			From:    e.id,
			To:      i,
			Request: true,
		}
	}

	// setting all the alive node as emppty after end of the program
	e.alive = nil

	// fmt.Println("alive: ", e.alive)
	// fmt.Println("suspected: ", e.suspected)
	// fmt.Println("delay: ", e.delay)
	// fmt.Println("id: ", e.id)
	// e.timeoutSignal = time.NewTicker(e.delay)
	// e.suspected = nil
}
