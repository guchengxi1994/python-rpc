'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-04-30 17:09:53
@LastEditors: xiaoshuyui
@LastEditTime: 2020-04-30 17:34:49
'''

import sys
sys.path.append("..")
import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))
    print("received: " + response.text)

if __name__ == '__main__':
    run()