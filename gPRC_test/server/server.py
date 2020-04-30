'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-30 17:16:02
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-30 17:34:38
'''
import sys
sys.path.append("..")

import grpc
import time
from concurrent import futures
from example import data_pb2, data_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'

class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = request.text
        return data_pb2.Data(text=str.upper())

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    serve()