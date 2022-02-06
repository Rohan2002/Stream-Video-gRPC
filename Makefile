PROTO_DIR = protos
OUT_DIR = $(PROTO_DIR)/proto_definations
PY_OUT_DIR = vidservice/proto_definations
TS_OUT_DIR = vidview/src/proto_definations
STREAM_PROTO_FILE = $(PROTO_DIR)/video-streaming.proto
PROTOC_GEN_TS_PATH= ./node_modules/.bin/protoc-gen-ts

proto-compile-py:
	python -m grpc_tools.protoc -I=$(PROTO_DIR)  --python_out=${PY_OUT_DIR} --grpc_python_out=${PY_OUT_DIR} $(STREAM_PROTO_FILE) \
	&& sed -i '' -e 's/import video_streaming_pb2 as video__streaming__pb2/import vidservice.proto_definations.video_streaming_pb2 as video__streaming__pb2/g' \
	${PY_OUT_DIR}/video_streaming_pb2_grpc.py

proto-compile-ts:
	protoc -I=$(PROTO_DIR) \
	--plugin="protoc-gen-ts=${PROTOC_GEN_TS_PATH}" \
	--js_out=import_style=commonjs,binary:$(TS_OUT_DIR) \
	--ts_out="service=grpc-web:${TS_OUT_DIR}" \
	$(STREAM_PROTO_FILE)

check-grpc:
	python3 -c "import grpc; print(grpc.__version__)"

run-client:
	python3 -m vidservice.py_client.client

run-server:
	python3 -m vidservice.back_end.server

clean-protos:
	rm -rf $(PY_OUT_DIR)/*.py && rm -rf $(TS_OUT_DIR)/*.js && rm -rf $(TS_OUT_DIR)/*.ts

# :)
fresh-protos-for-breakfast:
	make clean-protos && make proto-compile-ts && make proto-compile-py