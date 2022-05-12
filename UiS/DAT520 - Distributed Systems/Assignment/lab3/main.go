package main

import (
	"context"
	"dat520/lab3/failuredetector"
	"dat520/lab3/leaderdetector"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"os/signal"
	"sort"
	"syscall"
	"time"
)

const BufferSize = 1024

type main_server struct {
	connnection            *net.UDPConn
	failureDetectorObj     *failuredetector.EvtFailureDetector
	channelForOutHeartbeat chan failuredetector.Heartbeat
}

type client_serverInfo struct {
	connnection *net.UDPConn
	address     string
}

type client_server struct {
	connection_info map[int]*client_serverInfo
}

func (u *main_server) Close() {
	u.connnection.Close()
}

type EncodedHeartbeat struct {
	From    int  `json:"from"`
	To      int  `json:"to"`
	Request bool `json:"request"`
}

var server_list = map[int]string{
	1: "localhost:28010",
	2: "localhost:28020",
	3: "localhost:28030",
	4: "localhost:28040",
	5: "localhost:28050",
	6: "localhost:28060",
	7: "localhost:28070",
	8: "localhost:28080",
}

func main() {

	interruptSignal := make(chan os.Signal, 1)
	signal.Notify(interruptSignal, os.Interrupt, syscall.SIGTERM)

	node_lists := make([]int, 0, len(server_list))

	for k := range server_list {
		node_lists = append(node_lists, k)
	}
	sort.Ints(node_lists)

	for _, k := range node_lists {
		fmt.Println("Server id: ", k, " Server IP: ", server_list[k])
	}

	var serverID int
	fmt.Print("Enter your choice: ")
	fmt.Scan(&serverID)

	timeoutDelay := 1 * time.Second
	cleanExit, exit := context.WithCancel(context.Background())
	channelForOutHeartbeat := make(chan failuredetector.Heartbeat, len(node_lists))
	leaderDetectorObj := leaderdetector.NewMonLeaderDetector(node_lists)
	leaderSubscribe := leaderDetectorObj.Subscribe()
	failureDetectorObj := failuredetector.NewEvtFailureDetector(serverID, node_lists, leaderDetectorObj, timeoutDelay, channelForOutHeartbeat)

	udpServerObj := newUDPServer(server_list[serverID], failureDetectorObj, channelForOutHeartbeat)
	go udpServerObj.startUDPServer(cleanExit)

	own_node := &client_server{
		connection_info: make(map[int]*client_serverInfo),
	}

	for key, val := range server_list {
		address, errors := net.ResolveUDPAddr("udp", val)
		if errors != nil {
			log.Fatalf("Error: %s", errors)
		}
		connnection, errors := net.DialUDP("udp", nil, address)

		if errors != nil {
			log.Fatalf("Error: %s", errors)
		}
		con_details := &client_serverInfo{
			address:     val,
			connnection: connnection,
		}
		own_node.connection_info[key] = con_details
	}

	failureDetectorObj.Start()

	c := func(cleanExit context.Context, subs <-chan int) {
		for {
			select {
			case <-cleanExit.Done():
				return
			case leader := <-subs:
				log.Println("|---------------------------------------------------|")
				log.Println("|\tNew leader is : ", leader)
				log.Println("|\tLeader", leader, " IP address: ", server_list[leader])
				log.Println("|---------------------------------------------------|")
			}
		}
	}

	go c(cleanExit, leaderSubscribe)
	go broadcast_hb(cleanExit, own_node, channelForOutHeartbeat)

	<-interruptSignal
	exit()
	own_node.Close()
}

// send the heartbeats to the other nodes
func broadcast_hb(cleanExit context.Context, client *client_server, channelForOutHeartbeat chan failuredetector.Heartbeat) {
	// heartbeat encoded to json

	for {
		select {
		case <-cleanExit.Done():
			return

		case hb := <-channelForOutHeartbeat:

			if !hb.Request {
				log.Printf("Sending : %+v", hb)
			}
			newHeartbeat := EncodedHeartbeat{
				From:    hb.From,
				To:      hb.To,
				Request: hb.Request,
			}
			payload, err := json.Marshal(newHeartbeat)
			if err != nil {
				continue
			}

			udpInfo := client.connection_info[hb.To]
			udpInfo.connnection.Write(payload)
		}
	}
}

func newUDPServer(addr string, failureDetectorObj *failuredetector.EvtFailureDetector,
	channelForOutHeartbeat chan failuredetector.Heartbeat) *main_server {

	udpServerObj_dddress, errors := net.ResolveUDPAddr("udp", addr)

	if errors != nil {
		log.Fatalf("Error: %s", errors)
		//udpServerObj_dddress = nil
	}

	connection, errors := net.ListenUDP("udp", udpServerObj_dddress)

	if errors != nil {
		log.Fatalf("Error: %s", errors)
		//connection = nil
	}

	return &main_server{
		connnection:            connection,
		failureDetectorObj:     failureDetectorObj,
		channelForOutHeartbeat: channelForOutHeartbeat,
	}

}

// ServeUDP start listening to incoming requests
func (m *main_server) startUDPServer(cleanExit context.Context) {
	for {
		select {
		case <-cleanExit.Done():
			m.Close()
			return
		default:
			var temp_storage [BufferSize]byte

			n, address, errors := m.connnection.ReadFromUDP(temp_storage[0:])
			if errors != nil {
				log.Printf("Error: %s", errors)
				continue
			}
			c := func(addr *net.UDPAddr, req []byte) {
				var hb failuredetector.Heartbeat
				errors := json.Unmarshal(req, &hb)
				if errors != nil {
					log.Printf("Error: %v", errors)
				}
				m.failureDetectorObj.DeliverHeartbeat(hb)
			}

			go c(address, temp_storage[:n])
		}
	}
}

func (c *client_server) Close() {
	for _, v := range c.connection_info {
		v.connnection.Close()
	}
}
