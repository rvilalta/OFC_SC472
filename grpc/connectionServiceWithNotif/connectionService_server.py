from concurrent import futures
import time
import logging
import grpc

import connectionServiceWithNotif_pb2
import connectionServiceWithNotif_pb2_grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class connectionServiceWithNotif(connectionServiceWithNotif_pb2_grpc.ConnectionServiceWithNotifServicer):
    def __init__(self):
        self.connectionList = connectionServiceWithNotif_pb2.ConnectionList()

    def CreateConnection(self, request, context):
        logging.debug("Received Connection " + request.connectionId)
        self.connectionList.connection.extend([request])
        return google_dot_protobuf_dot_empty__pb2.Empty()

    def ListConnection(self, request, context):
        logging.debug("List Connections")
        return self.connectionList    
    def GetBer (self, request, context):
        logging.debug("Get Ber")
        while True:
            time.sleep(5)
            ber=connectionServiceWithNotif_pb2.Ber(value=10)
            yield ber


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connectionServiceWithNotif_pb2_grpc.add_ConnectionServiceWithNotifServicer_to_server(connectionServiceWithNotif(), server)
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
