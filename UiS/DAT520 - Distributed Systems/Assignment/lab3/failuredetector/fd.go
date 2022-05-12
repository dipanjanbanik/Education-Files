package failuredetector

import (
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
	for _, x := range nodeIDs {
		alive[x] = true
		// suspected[id] = false
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
			case z := <-e.hbIn:
				// delivering hearbeat reply
				if z.Request {
					// if e.hbresponse == true {
					e.hbSend <- Heartbeat{
						From:    e.id,
						To:      z.From,
						Request: false,
					}
					// } else if e.hbresponse == false {
				} else if !z.Request {
					e.alive[z.From] = true
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
}

// Stop stops e's main run loop.
func (e *EvtFailureDetector) Stop() {
	e.stop <- struct{}{}
}

func (e *EvtFailureDetector) timeout() {
	// condition to check and increase delay
	// if any suspected value is found then the function will increase the delay
	for i := range e.alive {
		if e.alive[i] && e.suspected[i] {
			e.delay = e.delay + e.delta
		}
	}

	for _, nodeId := range e.nodeIDs {
		// for the first time of a starting node this will mark other node
		// (except the node which we have just started) as suspected. it means
		// that other nodes are not online
		if !e.alive[nodeId] && !e.suspected[nodeId] {
			e.suspected[nodeId] = true
			e.sr.Suspect(nodeId)
			// fmt.Println("empty node: ", nodeId)
			// adding new node trigger this event. when a new node is added
			// this event restore the node and making suspected as false
		} else if e.alive[nodeId] && e.suspected[nodeId] {
			e.suspected[nodeId] = false
			e.sr.Restore(nodeId)
			// fmt.Println("added node: ", nodeId)
		}
		e.hbSend <- Heartbeat{
			To:      nodeId,
			From:    e.id,
			Request: true,
		}
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
				_ = 1
			} else {
				e.suspected[x] = true
			}
		}
	}

	e.alive = map[int]bool{}
}
