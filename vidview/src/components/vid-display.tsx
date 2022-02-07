/*
    Client interface to display videos.

*/
import React, { useState, useEffect } from "react";
import { VideoStreamerClient } from "../proto_definations/video-streaming_pb_service";
import {
  ClientStreamSignal,
  VideoMetaData,
} from "../proto_definations/video-streaming_pb";

const client = new VideoStreamerClient("http://0.0.0.0:8080");

// got data from https://github.com/improbable-eng/grpc-web/blob/master/client/grpc-web/docs/concepts.md#metadata
enum grpcCodes {
  OK,
  Canceled,
  Unknown,
  InvalidArgument,
  DeadlineExceeded,
  NotFound,
  AlreadyExists,
  PermissionDenied,
  ResourceExhausted,
  FailedPrecondition,
  Aborted,
  OutOfRange,
  Unimplemented,
  Internal,
  Unavailable,
  DataLoss,
  Unauthenticated,
}

const VidDisplay = () => {
  const CreateVideoRequest = (uuid_val: string) => {
    const video_meta = new VideoMetaData();
    video_meta.setValue(uuid_val);
    video_meta.setHtml(1);

    return video_meta;
  };
  const CreateVideoSignal = (start_stream: boolean) => {
    const client_signal = new ClientStreamSignal();
    const start_stream_signal = start_stream ? 1 : 0;
    client_signal.setSignal(start_stream_signal);

    return client_signal;
  };

  const VideoRequest = CreateVideoRequest(
    "e5aa32d3-b480-4ef7-9fb5-0303aab7a2cd"
  );
  const VideoStream = client.getVideoStream(VideoRequest);

  const [frame, setFrame] = useState<string>("");
  const [status, setStatus] = useState<any>();
  const [clientPlay, setClientPlay] = useState<boolean>(false);
  const [serverPlay, setServerPlay] = useState<boolean>(false);

  // Frame signal
  useEffect(() => {
    // client request: 1 meaning stream is on else 0 meaning stream is off.
    const signal = CreateVideoSignal(clientPlay);
    client.controlStream(signal, (error, response) => {
      if (error) {
        console.log(error);
      } else {
        const serverResponse = response?.getSignal();
        if (serverResponse == 1) {
          // server response: 1 meaning stream is on.
          setServerPlay(true);
        } else {
          // server response: 0 meaning stream is on.
          setServerPlay(false);
        }
      }
    });
  }, [clientPlay]);

  // Frame updater.
  useEffect(() => {
    VideoStream.on("data", (response: { getB64image: () => string }) => {
      const image: string = "data:image/png;base64," + response.getB64image(); // possible preprocessing of image here.
      try {
        setFrame(image);
      } catch (error) {
        console.log("Killing stream unexpectedly...have a nice day!");
        VideoStream.cancel();
      }
    });
  }, [clientPlay, serverPlay]);

  // // Frame HealthChecker
  useEffect(() => {
    if (frame && clientPlay) {
      VideoStream.on("status", (statuss: any) => {
        if (statuss != null) {
          setStatus(statuss);
        }
      });
    }
  }, [clientPlay, frame]);
  return (
    <div>
      <div>
        <h1>Status</h1>
        <p>
          <li>
            Status Code:{" "}
            {status != null ? grpcCodes[status.code] : "Not available"}
          </li>
          <li>
            Status Details: {status != null ? status.details : "Not available"}
          </li>
        </p>
      </div>
      <div>
        <h1>Video Display</h1>
        <div>
          <button onClick={() => setClientPlay(!clientPlay)}>
            {clientPlay ? "stop stream" : "start stream"}
          </button>
          <p>
            {serverPlay ? "Server is playing stream": "Server is not playing stream"}
          </p>
        </div>
        <div>
          <img src={frame} />
        </div>
      </div>
    </div>
  );
};

export default VidDisplay;
