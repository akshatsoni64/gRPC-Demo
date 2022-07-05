# gRPC Demo

## Setup:
- Clone the repository
```
git clone https://github.com/akshatsoni64/gRPC-Demo
```

- Create a virtual environment
```
python -m venv venv
```

- Fetch dependencies
```
pip install -r requirements.txt
```

- Code Generator Command
```
python -m grpc_tools.protoc -I<PATH> --python_out=<AUTO_GEN_CODE_PATH> --grpc_python_out=<AUTO_GEN_CODE_PATH> <PROTO_PATH>
```
Command Explanation:
```
python -m grpc_tools.protoc : The command which executes proto auto-code generation
```

```
-I<PATH> : PATH = The path where proto file might be residing, Don't put space after -I
```

```
--python_out=<AUTO_GEN_CODE_PATH>: AUTO_GEN_CODE_PATH = The path where auto generated code should be stored
```

```
--grpc_python_out=<AUTO_GEN_CODE_PATH>: AUTO_GEN_CODE_PATH = The path where auto generated code should be stored
```

```
<PROTO_PATH> : The exact path of proto file
```
Example: 
```
python -m grpc_tools.protoc : The command which executes proto auto-code generation
```

After the code generation following files will be generated:
```
<package_name>_pb2.py
<package_name>_pb2_grpc.py
```

- Implement the server & client (server.py & client.py)

- Fire up server
```
python server.py
```

- Start the client:
```
python client.py
```