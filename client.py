import logging
import grpc

from code import hello_pb2
from code import hello_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8088') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name=input("What's your name buddy?\n")))
    print("Greeter client received: " + response.message)


if __name__=="__main__":
    logging.basicConfig()
    run()