from concurrent import futures
import time
import logging
import grpc

import topologyService_pb2
import topologyService_pb2_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class topologyService(topologyService_pb2_grpc.TopologyServiceServicer):
    def __init__(self):
        self.topology = topologyService_pb2.Topology()
        node1=self.topology.node.add()
        node1.node_id = "node1"
        portA = node1.port.add()
        portA.port_id = "node1portA"
        node2=self.topology.node.add()
        node2.node_id = "node2"
        portB=node2.port.add()
        portB.port_id = "node2portA"
        link=self.topology.link.add()
        link.link_id = "link1"
        link.source_node = "node1"
        link.target_node = "node2"
        link.source_port = "node1portA"
        link.target_port = "node2portA"

    def GetTopology(self, request, context):
        logging.debug("Get Topology")
        return self.topology   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    topologyService_pb2_grpc.add_TopologyServiceServicer_to_server(topologyService(), server)
    server.add_insecure_port('[::]:50051')
    logging.debug("Starting server")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()
