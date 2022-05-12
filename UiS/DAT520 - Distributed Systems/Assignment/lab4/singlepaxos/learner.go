package singlepaxos

// Learner represents a learner as defined by the single-decree Paxos
// algorithm.
type Learner struct {
	// Add needed fields
	// Tip: you need to keep the decided values by the Paxos nodes somewhere
	id            int
	totalNoNodes  int
	rndCurrent    Round
	valuesLearned []values
}

type values struct {
	From  int
	Round Round
	Value Value
}

// NewLearner returns a new single-decree Paxos learner. It takes the
// following arguments:
//
// id: The id of the node running this instance of a Paxos learner.
//
// nrOfNodes: The total number of Paxos nodes.
func NewLearner(id int, nrOfNodes int) *Learner {
	return &Learner{
		id:           id,
		totalNoNodes: nrOfNodes,
		rndCurrent:   NoRound,
	}
}

// handleLearn processes learn lrn according to the single-decree
// Paxos algorithm. If handling the learn results in learner l emitting a
// corresponding decided value, then output will be true and val contain the
// decided value. If handleLearn returns false as output, then val will have
// its zero value.
func (l *Learner) handleLearn(learn Learn) (val Value, output bool) {
	if learn.Rnd < l.rndCurrent {
		return val, false
	} else if learn.Rnd > l.rndCurrent {
		l.rndCurrent = learn.Rnd
		l.valuesLearned = nil
	}

	if isNotExists(l.valuesLearned, learn.From) {
		return val, false
	}

	l.valuesLearned = append(l.valuesLearned, values{From: learn.From, Round: learn.Rnd, Value: learn.Val})

	if len(l.valuesLearned) < l.totalNoNodes/2+1 {
		return val, false
	}

	return learn.Val, true
}

func isNotExists(arr []values, element int) (output bool) {
	var result bool = false
	for _, x := range arr {
		if x.From == element {
			result = true
			break
		}
	}
	return result
}
