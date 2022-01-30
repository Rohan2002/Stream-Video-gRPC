proto-compile:
	 python -m grpc_tools.protoc -I ./vidservice/protos --python_out=./vidservice/protos/protos_definations --grpc_python_out=./vidservice/protos/protos_definations ./vidservice/protos/video-streaming.proto

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 -m vidservice.py_client.client

run-server:
	python3 -m vidservice.back_end.server