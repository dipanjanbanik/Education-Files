package main

import (
	"context"
	pb "dat520/lab2/grpc/proto"
	"fmt"
	"time"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:12111", grpc.WithInsecure())

	if err != nil {
		print("did not connect: %s", err)
	}
	defer conn.Close()
	client := pb.NewKeyValueServiceClient(conn)

	insertrequest := pb.InsertRequest{
		Key:   "1",
		Value: "one",
	}
	insertctx, insertcancel := context.WithTimeout(context.Background(), time.Second)
	defer insertcancel()
	insertresponse, err := client.Insert(insertctx, &insertrequest)
	if err != nil {
		print(err)
	}
	_ = insertresponse
	fmt.Println(insertrequest)

	lookuprequest := pb.LookupRequest{Key: "1"}
	lookupctx, lookupcancel := context.WithTimeout(context.Background(), time.Second)
	defer lookupcancel()
	lookupresponse, lookuperr := client.Lookup(lookupctx, &lookuprequest)
	if err != nil {
		print(lookuperr)
	}
	_ = lookupresponse
	fmt.Println(lookuprequest)

	keyrequest := pb.LookupRequest{}
	keyctx, keycancel := context.WithTimeout(context.Background(), time.Second)
	defer keycancel()
	keyresponse, keyuperr := client.Lookup(keyctx, &keyrequest)
	if err != nil {
		print(keyuperr)
	}
	_ = keyresponse
	fmt.Println(keyrequest)
}
