#! /usr/bin/env python3
from __future__ import print_function
import connection_pb2
import sys


# Iterates though all connections in the ConnectionList and prints info about them.
def ListConnections(connectionList):
  for connection in connectionList.connection:
    print("connectionID:", connection.connectionId)
    print("  sourceNode:", connection.sourceNode)
    print("  targetNode:", connection.targetNode)
    print("  sourcePort:", connection.sourcePort)  
    print("  targetPort:", connection.targetPort)
    print("  bandwidth:", connection.bandwidth)       
    if connection.layerProtocolName == connection_pb2.Connection.ETH:
      print("  layerProtocolName:ETH")
    elif connection.layerProtocolName == connection_pb2.Connection.OPTICAL:
      print("  layerProtocolName:OPTICAL")


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "CONNECTION_FILE")
    sys.exit(-1)
  
  connectionList = connection_pb2.ConnectionList()
  
  # Read the existing address book.
  with open(sys.argv[1], "rb") as f:
    connectionList.ParseFromString(f.read())
  
  ListConnections(connectionList)
