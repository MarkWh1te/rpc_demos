> this repo contains some simple examples of rpc 
 
# grpc demo
## install dependency 

```bash
pip install grpcio
pip install protobuf
pip install grpcio-tools
```


## generate python file from protobuf file

```bash
cd simple_grpc
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto
```

## write server and client file

## run server and client

```bash
python server.py
python client.py
```
and you will see
```
<grpc._channel.Channel object at 0x7f435d852a90>
<data_pb2_grpc.FormatDataStub object at 0x7f43597a8be0>
received: HELLO,WORLD!
```