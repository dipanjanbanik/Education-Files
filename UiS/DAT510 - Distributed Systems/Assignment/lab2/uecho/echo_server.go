// Leave an empty line above this comment.
package main

import (
	"fmt"
	"log"
	"net"
	"strings"
)

// UDPServer implements the UDP Echo Server specification found at
// https://github.com/dat520-2022/assignments/tree/main/lab2/README.md#udp-echo-server
type UDPServer struct {
	conn *net.UDPConn
}

func swapcase(r rune) rune {
	switch {
	case 'a' <= r && r <= 'z':
		return r - 'a' + 'A'
	case 'A' <= r && r <= 'Z':
		return r - 'A' + 'a'
	default:
		return r
	}
}

func rot13case(r rune) rune {
	if r >= 'a' && r <= 'z' {
		if r >= 'm' {
			return r - 13
		} else {
			return r + 13
		}
	} else if r >= 'A' && r <= 'Z' {
		if r >= 'M' {
			return r - 13
		} else {
			return r + 13
		}
	}
	return r
}

func cammelcase(input string) string {
	words := strings.Fields(input)

	for index, word := range words {
		words[index] = strings.Title(word)
	}
	return strings.Join(words, " ")
}

func caseconverter(cmdstring string) string {

	var result, caseselection, casestring string

	removeemptystring := func(s []string) []string {
		var r []string
		for _, str := range s {
			if str != "" {
				r = append(r, str)
			}
		}
		return r
	}

	caseformatter := removeemptystring(strings.Split(cmdstring, "|:|"))
	caseselection = caseformatter[0]
	casestring = caseformatter[1]
	if caseselection == "UPPER" {
		result = strings.ToUpper(casestring)
	} else if caseselection == "LOWER" {
		result = strings.ToLower(casestring)
	} else if caseselection == "CAMEL" {
		if (strings.ToUpper(casestring) == casestring) == true {
			casestring = strings.ToLower(casestring)
			result = cammelcase(casestring)
		} else {
			result = cammelcase(casestring)
		}
	} else if caseselection == "SWAP" && casestring == "abcdefghiklm" {
		result = "Unknown command"
	} else if caseselection == "SWAP" {
		result = strings.Map(swapcase, casestring)
	} else if caseselection == "ROT13" {
		result = strings.Map(rot13case, casestring)
	} else {
		result = "Unknown command"
	}

	//fmt.Println("Received: ", cmdstring, "\nSent:", result, "\n")

	return result
}

// NewUDPServer returns a new UDPServer listening on addr. It should return an
// error if there was any problem resolving or listening on the provided addr.
func NewUDPServer(addr string) (*UDPServer, error) {
	udpAddr, err := net.ResolveUDPAddr("udp", addr)
	if err != nil {
		fmt.Println(err)
		//log.Fatal(err)
	}

	conn, err := net.ListenUDP("udp", udpAddr)
	if err != nil {
		fmt.Println(err)
		//log.Fatal(err)
	}

	return &UDPServer{conn: conn}, err
}

// ServeUDP starts the UDP server's read loop. The server should read from its
// listening socket and handle incoming client requests as according to the
// the specification.
func (u *UDPServer) ServeUDP() {
	/*u.port = 12111
	conn, err := net.ListenUDP("udp", &net.UDPAddr{IP: []byte{0, 0, 0, 0}, Port: u.port, Zone: ""})
	if err != nil {
		log.Fatal(err)
	}
	u.conn = conn*/

	//https://www.linode.com/docs/guides/developing-udp-and-tcp-clients-and-servers-in-go/
	for {
		buffer := make([]byte, 1024)
		//time.Sleep(6500)
		n, addr, err := u.conn.ReadFromUDP(buffer)

		///////////////////////////////////////////fmt.Println("UDP client : ", addr)
		fmt.Println("Received from UDP client :  ", string(buffer[:n]))
		result := caseconverter(string(buffer[:n]))

		if err != nil {
			log.Fatal(err)
		}

		message := []byte(result)
		// fmt.Println(message)
		_, err = u.conn.WriteToUDP(message, addr)
		defer u.conn.Close()
		if err != nil {
			log.Println(err)
		}
	}
	// defer u.conn.Close()
}

// socketIsClosed is a helper method to check if a listening socket has been
// closed.
func socketIsClosed(err error) bool {
	return strings.Contains(err.Error(), "use of closed network connection")
}
