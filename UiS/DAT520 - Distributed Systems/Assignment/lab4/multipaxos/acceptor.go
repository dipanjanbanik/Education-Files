package multipaxos

// Acceptor represents an acceptor as defined by the Multi-Paxos algorithm.
type Acceptor struct {
	// NEED TO WORK HERE
	id  int
	rnd Round
}

// NewAcceptor returns a new Multi-Paxos acceptor.
// It takes the following arguments:
//
// id: The id of the node running this instance of a Paxos acceptor.
func NewAcceptor(id int) *Acceptor {
	// NEED TO WORK HERE
	return &Acceptor{
		id:  id,
		rnd: NoRound,
	}
}

// handlePrepare processes prepare prp according to the Multi-Paxos
// algorithm. If handling the prepare results in acceptor a emitting a
// corresponding promise, then output will be true and prm contain the promise.
// If handlePrepare returns false as output, then prm will be a zero-valued
// struct.
func (a *Acceptor) handlePrepare(prp Prepare) (prm Promise, output bool) {
	// NEED TO WORK HERE
	if prp.Crnd >= a.rnd {
		var slotSequence []PromiseSlot
		a.rnd = prp.Crnd
		return Promise{
			To:    prp.From,
			From:  a.id,
			Rnd:   a.rnd,
			Slots: slotSequence}, true
	}
	return prm, false
}

// handleAccept processes accept acc according to the Multi-Paxos
// algorithm. If handling the accept results in acceptor a emitting a
// corresponding learn, then output will be true and lrn contain the learn.  If
// handleAccept returns false as output, then lrn will be a zero-valued struct.
func (a *Acceptor) handleAccept(acc Accept) (lrn Learn, output bool) {
	// NEED TO WORK HERE
	if acc.Rnd >= a.rnd {
		return Learn{
			From: a.id,
			Slot: acc.Slot,
			Rnd:  acc.Rnd,
			Val:  acc.Val}, true
	}
	return lrn, false
}

// NEED TO WORK HERE
