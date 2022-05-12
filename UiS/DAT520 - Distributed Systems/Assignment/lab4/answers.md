## Answers to Paxos Questions 

You should write down your answers to the [questions](README.md#questions) for Lab 4 in this file.

1. It is possible that Paxos enters an infinite loop when different proposers sends higher rounds.

2. The value to agree on is not included in the Prepare messages. Only the current round number is included.

3. Yes, Paxos rely on an increasing proposal/round number. Paxos need to know the current state of each node and by increasing the round number it can detect the transitions and able to execute decision fo the next stage.

4. The "value last accepted" is the most recent value that an acceptor got from the proposer in an ACCEPT message. For single paxos this value is the acceptors current state.

5. The simplest consensus procedure will have only one acceptor. We can assign this function to one of our distributed systems. Multiple proposers will make multiple value suggestions. The acceptor selects one of these options. However, this does not manage acceptor crashes. If it crashes after selecting a value, we won't know what it was and must wait for the acceptor to restart. We want to develop a system that works when most nodes are up.
Reference - https://people.cs.rutgers.edu/~pxk/417/notes/paxos.html

6. There might be some possibilities that two proposers both believe themselves to be the leader and send `Prepare` messages. If the round number is differnt from each other there might be a possibility that they want to be act as a leader.

7. Your answer.

8. This is not possible. This accepted value will be sent as the latest accepted value in all future promise messages from an acceptor that has promised to a proposer. Each time a new value is proposed, the acceptors return the previously accepted value, which must be used. A new value must be agreed upon by the algorithm.

9. To choose a value, a Proposer must receive promises and send an Accept message to Acceptors. Their chosen value is broadcast in a Learn message. Acceptors send Learn messages to Learners. The value is learned if they get Learn signals from more than half of the acceptors. The learned value is the final chosen value for that distributed system.
