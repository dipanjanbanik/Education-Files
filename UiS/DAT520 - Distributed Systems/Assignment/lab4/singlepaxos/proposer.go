package singlepaxos

// Proposer represents a proposer as defined by the single-decree Paxos
// algorithm.
type Proposer struct {
	crnd         Round
	clientValue  Value
	id           int
	totalNodes   int
	acceptValues []Accept
}

// NewProposer returns a new single-decree Paxos proposer.
// It takes the following arguments:
//
// id: The id of the node running this instance of a Paxos proposer.
//
// nrOfNodes: The total number of Paxos nodes.
//
// The proposer's internal crnd field should initially be set to the value of
// its id.
func NewProposer(id int, nrOfNodes int) *Proposer {
	return &Proposer{
		crnd:         Round(id),
		clientValue:  ZeroValue,
		id:           id,
		totalNodes:   nrOfNodes,
		acceptValues: []Accept{},
	}
}

// handlePromise processes promise prm according to the single-decree
// Paxos algorithm. If handling the promise results in proposer p emitting a
// corresponding accept, then output will be true and acc contain the promise.
// If handlePromise returns false as output, then acc will be a zero-valued
// struct.
func (p *Proposer) handlePromise(prm Promise) (acc Accept, output bool) {

	// if given round is not matching with current round then
	// it will return false
	switch {
	case prm.Rnd > p.crnd:
		return Accept{}, false
	case prm.Rnd < p.crnd:
		return Accept{}, false
	}

	// if promise from is matching with NewProposer id(from) it will
	// return false because leader node must not be equal to promise from
	for _, i := range p.acceptValues {
		if i.From == prm.From {
			return Accept{}, false
		}
	}

	// appending values in a acceptValues struct which similer to the Accept
	p.acceptValues = append(p.acceptValues, Accept{
		From: prm.From,
		Rnd:  prm.Vrnd,
		Val:  prm.Vval})

	// if there is some value exits in acceptValues
	if len(p.acceptValues) > (p.totalNodes / 2) {
		largeProposer := Accept{}
		// check if round value is higher. if higher found save the result in
		// largeProposer which similer to the Accept
		for _, i := range p.acceptValues {
			if i.Rnd > largeProposer.Rnd {
				largeProposer = i
			}
		}

		// if it is NoRound return empty string
		if largeProposer.Rnd == NoRound {
			if p.clientValue == ZeroValue {
				p.clientValue = Value("")
			}

			// if it is ZeroValue return empty string
		} else if largeProposer.Val == ZeroValue {
			if p.clientValue == ZeroValue {
				p.clientValue = Value("")
			}

			// if NoRound and ZeroValue are no satisfied then return the value
		} else {
			p.clientValue = largeProposer.Val
			return Accept{
				From: p.id,
				Rnd:  p.crnd,
				Val:  p.clientValue}, true
		}
		return Accept{
			From: p.id,
			Rnd:  p.crnd,
			Val:  p.clientValue}, true
	}

	return Accept{}, false
}

// increaseCrnd increases proposer p's crnd field by the total number
// of Paxos nodes.
func (p *Proposer) increaseCrnd() {
	p.crnd += Round(p.totalNodes)
}
