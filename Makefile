proto-compile:
	 python -m grpc_tools.protoc -I ./protos --python_out=./protos/protos_definations --grpc_python_out=./protos/protos_definations ./protos/video-streaming.proto

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 -m py_client.client

run-server:
	python3 -m back_end.server