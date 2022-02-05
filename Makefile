PROTO_DIR = protos
OUT_DIR = $(PROTO_DIR)/proto_definations
STREAM_PROTO_FILE = $(PROTO_DIR)/video-streaming.proto
PROTOC_GEN_TS_PATH= ./node_modules/.bin/protoc-gen-ts

proto-compile-py:
	python -m grpc_tools.protoc -I=$(PROTO_DIR)  --python_out=${OUT_DIR} --grpc_python_out=${OUT_DIR} $(STREAM_PROTO_FILE) \
	&& sed -i '' -e 's/import video_streaming_pb2 as video__streaming__pb2/import protos.proto_definations.video_streaming_pb2 as video__streaming__pb2/g' \
	${OUT_DIR}/video_streaming_pb2_grpc.py

proto-compile-ts:
	protoc -I=$(PROTO_DIR) \
	--plugin="protoc-gen-ts=${PROTOC_GEN_TS_PATH}" \
	--js_out=import_style=commonjs,binary:$(OUT_DIR) \
	--ts_out="service=grpc-web:${OUT_DIR}" \
	$(STREAM_PROTO_FILE)

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 -m vidservice.py_client.client

run-server:
	python3 -m vidservice.back_end.server

clean-protos:
	rm -rf $(OUT_DIR)/*.py && rm -rf $(OUT_DIR)/*.js && rm -rf $(OUT_DIR)/*.ts

# :)
fresh-protos-for-breakfast:
	make clean-protos && make proto-compile-ts && make proto-compile-py