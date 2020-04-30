<!--
 * @lanhuage: markdown
 * @Descripttion: 
 * @version: beta
 * @Author: xiaoshuyui
 * @Date: 2020-04-30 17:40:23
 * @LastEditors: xiaoshuyui
 * @LastEditTime: 2020-04-30 17:40:55
 -->
#### generate proto-related py files

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto