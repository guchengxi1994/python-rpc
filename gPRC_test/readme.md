<!--
 * @lanhuage: markdown
 * @Descripttion: 
 * @version: beta
 * @Author: xiaoshuyui
 * @Date: 2020-04-30 17:40:23
 * @LastEditors: xiaoshuyui
 * @LastEditTime: 2020-05-06 14:59:19
 -->
#### generate proto-related py files

eg.python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto