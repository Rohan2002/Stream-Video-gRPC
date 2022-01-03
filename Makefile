proto-compile:
	 python -m grpc_tools.protoc -I ./protos --python_out=./protos_configuration --grpc_python_out=./protos_configuration ./protos/video-streaming.proto

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 ping-client.py

run-server:
	python3 pong-server.py