'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-06 15:01:47
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-06 17:03:37
'''
import sys
sys.path.append("..")


import grpc
# import data_pb2, data_pb2_grpc
from uploadImg import upload_pb2,upload_pb2_grpc
import cv2
import base64
import numpy as np

# SIZE = 219034
 
_HOST = 'localhost'
_PORT = '8080'
# class FormatData(data_pb2_grpc.FormatDataServicer):
#     # 重写接口函数.输入和输出都是proto中定义的Data类型
#     def DoFormat(self, request, context):
#         str = request.text
#         return data_pb2.actionresponse(text=str.upper())  # 返回一个类实例


def img2base64(imgpath):
    with open(imgpath,'rb') as f:
        return base64.b64encode(f.read())
    
 
def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    # print(conn)
    client = upload_pb2_grpc.UploadStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    # print(client)
    imgPath = "D:\\testALg\\py_rpc\\python-rpc\\gPRC_test\\test\\lena.png"
    
    # img = cv2.imread(imgPath)
    # s = base64.b64encode(img)
    s = img2base64(imgPath)
    response = client.Fileup(upload_pb2.ImgRecRequest(data=s,name=imgPath,imgID=0))
    print(response)

 
 
if __name__ == '__main__':
    run()

