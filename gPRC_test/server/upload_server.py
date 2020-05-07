'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-06 15:08:01
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-06 17:01:56
'''
import sys
sys.path.append("..")

import threading
import grpc
from uploadImg import upload_pb2_grpc
from uploadImg import upload_pb2
import time
from concurrent import futures
import base64
from pprint import pprint
import os
import re
import cv2
import numpy as np
 
import PIL


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'
 
class Upload(upload_pb2_grpc.UploadServicer):
    def Fileup(self, request, context):
        # return super().Fileup(request, context)
        imgText = request.data 
        imgname = request.name
        print(imgname)

        decode_img = base64.b64decode(imgText)
        # img = np.fromstring(decode_img,dtype=np.int8)
        # img = np.reshape(img,(512,512,3))
        with open("./test.png",'wb') as f:
            f.write(decode_img)

        # cv2.imwrite("./test.png",img)

        return upload_pb2.Response(code=200)


def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))   # 创建一个服务器
    upload_pb2_grpc.add_UploadServicer_to_server(Upload(), grpcServer)  # 在服务器中添加派生的接口服务（自己实现了处理函数）
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)    # 添加监听端口
    grpcServer.start()    #  启动服务器
    try:
        while True:
            print('start===============>')
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0) # 关闭服务器
 
 
if __name__ == '__main__':
    serve()




