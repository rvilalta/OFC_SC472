#! /usr/bin/env python3
import connection_pb2
import sys

try:
  raw_input          # Python 2
except NameError:
  raw_input = input  # Python 3


# This function fills in a Connection message based on user input.
def PromptForConnection(connection):
  connection.connectionId = raw_input("Enter connectionID: ")
  connection.sourceNode = raw_input("Enter sourceNode: ")  
  connection.targetNode = raw_input("Enter targetNode: ")
  connection.sourcePort = raw_input("Enter sourcePort: ")  
  connection.targetPort = raw_input("Enter targetPort: ") 
  connection.bandwidth = int( raw_input("Enter bandwidth: ") )
  
  type = raw_input("Is this a eth or optical connection? ")
  if type == "eth":
    connection.layerProtocolName = connection_pb2.Connection.ETH
  elif type == "optical":
    connection.layerProtocolName = connection_pb2.Connection.OPTICAL
  else:
    print("Unknown layerProtocolName type; leaving as default value.")


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "CONNECTION_FILE")
    sys.exit(-1)
  
  connectionList = connection_pb2.ConnectionList()
  
  # Read the existing address book.
  try:
    with open(sys.argv[1], "rb") as f:
      connectionList.ParseFromString(f.read())
  except IOError:
    print(sys.argv[1] + ": File not found.  Creating a new file.")
  
  # Add an address.
  PromptForConnection(connectionList.connection.add())
  
  # Write the new address book back to disk.
  with open(sys.argv[1], "wb") as f:
    f.write(connectionList.SerializeToString())
