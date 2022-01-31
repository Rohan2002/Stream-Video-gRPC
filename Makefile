PROTO_DIR = ./protos
OUT_DIR = $(PROTO_DIR)/protos_definations
STREAM_PROTO_FILE = $(PROTO_DIR)/video-streaming.proto
PROTOC_GEN_TS_PATH= ./node_modules/.bin/protoc-gen-ts

proto-compile-py:
	python -m grpc_tools.protoc -I=$(PROTO_DIR) --python_out=$(OUT_DIR) --grpc_python_out=$(OUT_DIR) $(STREAM_PROTO_FILE)

proto-compile-js:
	protoc -I=$(PROTO_DIR) \
	--js_out=import_style=commonjs,binary:$(OUT_DIR) \
	--grpc-web_out=import_style=typescript,mode=grpcweb:$(OUT_DIR) \
	$(STREAM_PROTO_FILE)

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 -m vidservice.py_client.client

run-server:
	python3 -m vidservice.back_end.server

#  --js_out=import_style=commonjs,binary:$(OUT_DIR)  