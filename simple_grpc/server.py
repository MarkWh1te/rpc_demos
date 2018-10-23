"""Server side of grpc demo
"""
import grpc
import time
from concurrent import futures
import data_pb2
import data_pb2_grpc

_ONE_DAY_IN_SECONDS = 3
# _ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'


class FormatData(data_pb2_grpc.FormatDataServicer):
    # settting input and output from protobuf file
    def DoFormat(self, request, context):
        str = request.text
        time.sleep(3)
        return data_pb2.actionresponse(text=str.upper())


def serve():
    # setup grpc server
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    # add function to grpc server
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    # set up hot and port server list to
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    # start grpc server
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
