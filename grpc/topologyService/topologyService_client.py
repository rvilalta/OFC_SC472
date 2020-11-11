from __future__ import print_function

import grpc

import topologyService_pb2
import topologyService_pb2_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
try:
  raw_input          # Python 2
except NameError:
  raw_input = input  # Python 3


def getTopology():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = topologyService_pb2_grpc.TopologyServiceStub(channel)
        response = stub.GetTopology(google_dot_protobuf_dot_empty__pb2.Empty())
    print("TopologyService client received: " + str(response) )

if __name__ == '__main__':
    getTopology()
