// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package proto

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// KeyValueServiceClient is the client API for KeyValueService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type KeyValueServiceClient interface {
	Insert(ctx context.Context, in *InsertRequest, opts ...grpc.CallOption) (*InsertResponse, error)
	Lookup(ctx context.Context, in *LookupRequest, opts ...grpc.CallOption) (*LookupResponse, error)
	Keys(ctx context.Context, in *KeysRequest, opts ...grpc.CallOption) (*KeysResponse, error)
}

type keyValueServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewKeyValueServiceClient(cc grpc.ClientConnInterface) KeyValueServiceClient {
	return &keyValueServiceClient{cc}
}

func (c *keyValueServiceClient) Insert(ctx context.Context, in *InsertRequest, opts ...grpc.CallOption) (*InsertResponse, error) {
	out := new(InsertResponse)
	err := c.cc.Invoke(ctx, "/proto.KeyValueService/Insert", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *keyValueServiceClient) Lookup(ctx context.Context, in *LookupRequest, opts ...grpc.CallOption) (*LookupResponse, error) {
	out := new(LookupResponse)
	err := c.cc.Invoke(ctx, "/proto.KeyValueService/Lookup", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *keyValueServiceClient) Keys(ctx context.Context, in *KeysRequest, opts ...grpc.CallOption) (*KeysResponse, error) {
	out := new(KeysResponse)
	err := c.cc.Invoke(ctx, "/proto.KeyValueService/Keys", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// KeyValueServiceServer is the server API for KeyValueService service.
// All implementations must embed UnimplementedKeyValueServiceServer
// for forward compatibility
type KeyValueServiceServer interface {
	Insert(context.Context, *InsertRequest) (*InsertResponse, error)
	Lookup(context.Context, *LookupRequest) (*LookupResponse, error)
	Keys(context.Context, *KeysRequest) (*KeysResponse, error)
	mustEmbedUnimplementedKeyValueServiceServer()
}

// UnimplementedKeyValueServiceServer must be embedded to have forward compatible implementations.
type UnimplementedKeyValueServiceServer struct {
}

func (UnimplementedKeyValueServiceServer) Insert(context.Context, *InsertRequest) (*InsertResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Insert not implemented")
}
func (UnimplementedKeyValueServiceServer) Lookup(context.Context, *LookupRequest) (*LookupResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Lookup not implemented")
}
func (UnimplementedKeyValueServiceServer) Keys(context.Context, *KeysRequest) (*KeysResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Keys not implemented")
}
func (UnimplementedKeyValueServiceServer) mustEmbedUnimplementedKeyValueServiceServer() {}

// UnsafeKeyValueServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to KeyValueServiceServer will
// result in compilation errors.
type UnsafeKeyValueServiceServer interface {
	mustEmbedUnimplementedKeyValueServiceServer()
}

func RegisterKeyValueServiceServer(s grpc.ServiceRegistrar, srv KeyValueServiceServer) {
	s.RegisterService(&KeyValueService_ServiceDesc, srv)
}

func _KeyValueService_Insert_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(InsertRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KeyValueServiceServer).Insert(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.KeyValueService/Insert",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KeyValueServiceServer).Insert(ctx, req.(*InsertRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _KeyValueService_Lookup_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LookupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KeyValueServiceServer).Lookup(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.KeyValueService/Lookup",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KeyValueServiceServer).Lookup(ctx, req.(*LookupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _KeyValueService_Keys_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(KeysRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(KeyValueServiceServer).Keys(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.KeyValueService/Keys",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(KeyValueServiceServer).Keys(ctx, req.(*KeysRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// KeyValueService_ServiceDesc is the grpc.ServiceDesc for KeyValueService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var KeyValueService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "proto.KeyValueService",
	HandlerType: (*KeyValueServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Insert",
			Handler:    _KeyValueService_Insert_Handler,
		},
		{
			MethodName: "Lookup",
			Handler:    _KeyValueService_Lookup_Handler,
		},
		{
			MethodName: "Keys",
			Handler:    _KeyValueService_Keys_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "proto/kv.proto",
}
