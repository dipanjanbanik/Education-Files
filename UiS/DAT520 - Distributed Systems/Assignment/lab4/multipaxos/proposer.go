package multipaxos

import (
	"dat520/lab3/leaderdetector"
)

// Proposer represents a proposer as defined by the Multi-Paxos algorithm.
type Proposer struct {
	id           int
	quorum       int
	n            int
	crnd         Round
	adu          SlotID
	nextSlot     SlotID
	promises     []*Promise
	promiseCount int
	ld           leaderdetector.LeaderDetector
	leader       int
}

// NewProposer returns a new Multi-Paxos proposer. It takes the following
// arguments:
//
// id: The id of the node running this instance of a Paxos proposer.
//
// nrOfNodes: The total number of Paxos nodes.
//
// adu: all-decided-up-to. The initial id of the highest _consecutive_ slot
// that has been decided. Should normally be set to -1 initially, but for
// testing purposes it is passed in the constructor.
//
// ld: A leader detector implementing the detector.LeaderDetector interface.
//
// The proposer's internal crnd field should initially be set to the value of
// its id.
func NewProposer(id, nrOfNodes, adu int, ld leaderdetector.LeaderDetector) *Proposer {
	return &Proposer{
		id:       id,
		quorum:   (nrOfNodes / 2) + 1,
		n:        nrOfNodes,
		crnd:     Round(id),
		adu:      SlotID(adu),
		nextSlot: 0,
		promises: make([]*Promise, nrOfNodes),
		ld:       ld,
		leader:   ld.Leader(),
	}
}

// handlePromise processes promise prm according to the Multi-Paxos
// algorithm. If handling the promise results in proposer p emitting a
// corresponding accept slice, then output will be true and accs contain the
// accept messages. If handlePromise returns false as output, then accs will be
// a nil slice.
func (p *Proposer) handlePromise(prm Promise) (accs []Accept, output bool) {
	// NEED TO WORK HERE
	return []Accept{
		{From: -1, Slot: -1, Rnd: -2},
	}, true
}
