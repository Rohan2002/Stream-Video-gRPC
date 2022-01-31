/**
 * @fileoverview gRPC-Web generated client stub for protos
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as video$streaming_pb from './video-streaming_pb';


export class VideoStreamerClient {
  client_: grpcWeb.AbstractClientBase;
  hostname_: string;
  credentials_: null | { [index: string]: string; };
  options_: null | { [index: string]: any; };

  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: any; }) {
    if (!options) options = {};
    if (!credentials) credentials = {};
    options['format'] = 'binary';

    this.client_ = new grpcWeb.GrpcWebClientBase(options);
    this.hostname_ = hostname;
    this.credentials_ = credentials;
    this.options_ = options;
  }

  methodDescriptorgetVideoStream = new grpcWeb.MethodDescriptor(
    '/protos.VideoStreamer/getVideoStream',
    grpcWeb.MethodType.SERVER_STREAMING,
    video$streaming_pb.VideoMetaData,
    video$streaming_pb.VideoFrames,
    (request: video$streaming_pb.VideoMetaData) => {
      return request.serializeBinary();
    },
    video$streaming_pb.VideoFrames.deserializeBinary
  );

  getVideoStream(
    request: video$streaming_pb.VideoMetaData,
    metadata?: grpcWeb.Metadata): grpcWeb.ClientReadableStream<video$streaming_pb.VideoFrames> {
    return this.client_.serverStreaming(
      this.hostname_ +
        '/protos.VideoStreamer/getVideoStream',
      request,
      metadata || {},
      this.methodDescriptorgetVideoStream);
  }

}

