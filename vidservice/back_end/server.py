import logging
from pathlib import Path
import grpc
from concurrent.futures import ThreadPoolExecutor
import logging
import numpy as np
import vidservice.back_end.streamer.streamer as streamer
from vidservice.proto_definations import (video_streaming_pb2_grpc, video_streaming_pb2)

class VideoServer(video_streaming_pb2_grpc.VideoStreamerServicer):
    def create_frame(self, frame: np.ndarray, shape):
        return video_streaming_pb2.VideoFrames(b64image=frame, width=shape[0], height = shape[1])

    def getVideoStream(self, request, context):
        # prepare video path based on uuid
        base_path = Path(__file__).parent.absolute().parents[1]
        video_file = f"{request.value}.mp4"
        video_uuid_path = base_path / "videos" / video_file

        # Get request
        should_encode_for_html = request.html == 1
        self.streamer_api = streamer.VideoStreamer(video_uuid_path, html=should_encode_for_html)
        self.streamer_api.init_video()

        # Prepare response
        frames = self.streamer_api.send_frame()
        
        # Yield response
        for frame, shape, status in frames:
            if not status:
                break
            yield self.create_frame(frame, shape)

        logging.info("All frames have been read, releasing video resources now....")
        self.streamer_api.release_video_resources()
        return
        # TODO: Why does this go in an infinite loop after resources are released (i.e. why are reader, writer threads spawned again in streamer api? Why is streamer api being called again?)

def serve(address: str) -> None:
    server = grpc.server(ThreadPoolExecutor(10))
    vid_serve = VideoServer()
    video_streaming_pb2_grpc.add_VideoStreamerServicer_to_server(vid_serve, server)
    server.add_insecure_port(address)
    server.start()
    logging.info("Server serving at %s", address)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve("0.0.0.0:50051")