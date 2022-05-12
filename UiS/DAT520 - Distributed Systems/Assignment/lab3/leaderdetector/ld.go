package leaderdetector

import (
	"reflect"
)

// A MonLeaderDetector represents a Monarchical Eventual Leader Detector as
// described at page 53 in:
// Christian Cachin, Rachid Guerraoui, and Luís Rodrigues: "Introduction to
// Reliable and Secure Distributed Programming" Springer, 2nd edition, 2011.
type MonLeaderDetector struct {
	id           int
	nodeid       []int
	sus          map[int]bool
	subscription []chan int
}

// NewMonLeaderDetector returns a new Monarchical Eventual Leader Detector
// given a list of node ids.
func NewMonLeaderDetector(nodeIDs []int) *MonLeaderDetector {
	var id int
	var channels []chan int
	sus := make(map[int]bool)

	if nodeIDs[len(nodeIDs)-1] < 0 {
		id = -1
	} else {
		id = nodeIDs[len(nodeIDs)-1]
	}

	m := &MonLeaderDetector{
		id:           id,
		nodeid:       nodeIDs,
		sus:          sus,
		subscription: channels,
	}
	return m
}

// Leader returns the current leader. Leader will return UnknownID if all nodes
// are sus.
func (m *MonLeaderDetector) Leader() int {
	maxRank := -1
	if reflect.DeepEqual(m.nodeid, m.sus) {
		maxRank = UnknownID
	} else {
		for _, nodeId := range m.nodeid {
			if !m.sus[nodeId] {
				if nodeId > maxRank {
					maxRank = nodeId
				}
			}
		}
	}
	m.id = maxRank
	return maxRank
}

// Suspect instructs the leader detector to consider the node with matching
// id as suspect. If the suspect indication result in a leader change
// the leader detector should publish this change to its subscription.
func (m *MonLeaderDetector) Suspect(id int) {
	if !m.sus[id] {
		m.sus[id] = true
		previousLeader := m.id
		m.Leader()
		if m.id != previousLeader {
			for _, val := range m.subscription {
				val <- m.id
			}
		}
	}
}

// Restore instructs the leader detector to consider the node with matching
// id as restored. If the restore indication result in a leader change
// the leader detector should publish this change to its subscription.
func (m *MonLeaderDetector) Restore(id int) {
	if m.sus[id] {
		m.sus[id] = false
		// delete(m.sus, id)
		previousLeader := m.id
		m.Leader()
		if m.id != previousLeader {
			for _, val := range m.subscription {
				val <- m.id
			}
		}
	}
}

// Subscribe returns a buffered channel which will be used by the leader
// detector to publish the id of the highest ranking node.
// The leader detector will publish UnknownID if all nodes become sus.
// Subscribe will drop publications to slow subscription.
// Note: Subscribe returns a unique channel to every subscriber;
// it is not meant to be shared.
func (m *MonLeaderDetector) Subscribe() <-chan int {
	c := make(chan int, 8)
	m.subscription = append(m.subscription, c)
	return c
}
