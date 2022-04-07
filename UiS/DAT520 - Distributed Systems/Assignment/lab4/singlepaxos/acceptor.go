package singlepaxos

// Acceptor represents an acceptor as defined by the single-decree Paxos
// algorithm.
type Acceptor struct {
	id       int
	maxRnd   Round
	maxVrnd  Round
	maxValue Value
}

// NewAcceptor returns a new single-decree Paxos acceptor.
// It takes the following arguments:
//
// id: The id of the node running this instance of a Paxos acceptor.
func NewAcceptor(id int) *Acceptor {
	return &Acceptor{
		id:       id,
		maxRnd:   NoRound,
		maxVrnd:  NoRound,
		maxValue: ZeroValue,
	}
}

// handlePrepare processes prepare prp according to the single-decree
// Paxos algorithm. If handling the prepare results in acceptor a emitting a
// corresponding promise, then output will be true and prm contain the promise.
// If handlePrepare returns false as output, then prm will be a zero-valued
// struct.
func (a *Acceptor) handlePrepare(prp Prepare) (prm Promise, output bool) {
	//if current round is less than the max round it returns false
	if prp.Crnd < a.maxRnd {
		return Promise{}, false
		// if current round is greater than the max round it sets the current round as max
	} else if prp.Crnd > a.maxRnd {
		a.maxRnd = prp.Crnd
		return Promise{
			To:   prp.From,
			From: a.id,
			Rnd:  a.maxRnd,
			Vrnd: a.maxVrnd,
			Vval: a.maxValue}, true
	}
	return
}

// handleAccept processes accept acc according to the single-decree
// Paxos algorithm. If handling the accept results in acceptor a emitting a
// corresponding learn, then output will be true and lrn contain the learn.  If
// handleAccept returns false as output, then lrn will be a zero-valued struct.
func (a *Acceptor) handleAccept(acc Accept) (lrn Learn, output bool) {
	// if current round is greater than the max round
	if acc.Rnd >= a.maxRnd {
		// if current round is not eqaul to Vrnd it saves the current value and returns it
		if acc.Rnd != a.maxVrnd {
			a.maxRnd = acc.Rnd
			a.maxVrnd = acc.Rnd
			a.maxValue = acc.Val
			return Learn{
				From: a.id,
				Rnd:  a.maxVrnd,
				Val:  a.maxValue}, true
		}
		//if current round is less than the max round it returns false
	} else if acc.Rnd < a.maxRnd {
		return Learn{}, false
	}
	return
}
