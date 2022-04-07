package multipaxos

// Learner represents a learner as defined by the Multi-Paxos algorithm.
type Learner struct {
	id            int
	totalNodes    int
	learnerValues map[SlotID][]Learn
	rnd           Round
}

// NewLearner returns a new Multi-Paxos learner. It takes the
// following arguments:
//
// id: The id of the node running this instance of a Paxos learner.
//
// nrOfNodes: The total number of Paxos nodes.
func NewLearner(id int, nrOfNodes int) *Learner {
	return &Learner{
		id:            id,
		totalNodes:    nrOfNodes,
		learnerValues: map[SlotID][]Learn{},
		rnd:           NoRound,
	}
}

// handleLearn processes learn lrn according to the Multi-Paxos
// algorithm. If handling the learn results in learner l emitting a
// corresponding decided value, then output will be true, sid the id for the
// slot that was decided and val contain the decided value. If handleLearn
// returns false as output, then val and sid will have their zero value.
func (l *Learner) handleLearn(learn Learn) (val Value, sid SlotID, output bool) {

	if learn.Rnd == l.rnd {

		// two learns for slot 1, 3 nodes, equal round and value,
		// same sender = no quorum -> no output
		for _, l := range l.learnerValues[learn.Slot] {
			if l.Rnd == learn.Rnd {
				if l.Slot == learn.Slot {
					if l.From == learn.From {
						return val, sid, false
					}
				}
			}
		}

		l.learnerValues[learn.Slot] = append(l.learnerValues[learn.Slot], learn)
		if len(l.learnerValues[learn.Slot]) == l.totalNodes/2+1 {
			return learn.Val, learn.Slot, true
		}

	} else if learn.Rnd < l.rnd {
		return val, sid, false
	} else {
		l.rnd = learn.Rnd
		l.learnerValues[learn.Slot] = []Learn{learn}
	}
	return val, sid, false
}
