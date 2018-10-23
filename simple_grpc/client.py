"""Client side of grpc
"""
import grpc
import data_pb2
import data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    print(client)
    # response is the class in protobuf file
    response = client.DoFormat(data_pb2.actionrequest(text='hello,world!'))
    print("received: " + response.text)
    # no blocking demo
    for i in range(10):
        # no blocking
        r = client.DoFormat.future(data_pb2.actionrequest(text='hello,world!'))
        # blocking
        #r = client.DoFormat(data_pb2.actionrequest(text='hello,world!'))
        print('fff')


if __name__ == '__main__':
    run()
