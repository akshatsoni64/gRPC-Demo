from concurrent import futures
import logging

import grpc
from code import hello_pb2
from code import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8088')
    server.start()
    server.wait_for_termination()


if __name__=="__main__":
    logging.basicConfig()
    serve()