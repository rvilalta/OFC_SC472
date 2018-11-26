from __future__ import print_function

import grpc

import connectionServiceWithNotif_pb2
import connectionServiceWithNotif_pb2_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
try:
  raw_input          # Python 2
except NameError:
  raw_input = input  # Python 3

def createConnection(stub):
    connection=connectionServiceWithNotif_pb2.Connection()
    connection.connectionId = raw_input("Enter connectionID: ")
    connection.sourceNode = raw_input("Enter sourceNode: ")  
    connection.targetNode = raw_input("Enter targetNode: ")
    connection.sourcePort = raw_input("Enter sourcePort: ")  
    connection.targetPort = raw_input("Enter targetPort: ") 
    connection.bandwidth = int( raw_input("Enter bandwidth: ") )

    response = stub.CreateConnection(connection)
    print("ConnectionService client received: " + str(response) )

def listConnection(stub):
    response = stub.ListConnection(google_dot_protobuf_dot_empty__pb2.Empty())
    print("ConnectionService client received: " + str(response) )

def getBer(stub):
    responses = stub.GetBer(connectionServiceWithNotif_pb2.Connection(connectionId="conn1"))
    for response in responses:
        print("Received Ber %s" % (response.value) )

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = connectionServiceWithNotif_pb2_grpc.ConnectionServiceWithNotifStub(channel)
        #createConnection(stub)
        listConnection(stub)
        getBer(stub)