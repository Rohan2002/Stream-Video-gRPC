import * as jspb from 'google-protobuf'



export class VideoMetaData extends jspb.Message {
  getValue(): UUID | undefined;
  setValue(value?: UUID): VideoMetaData;
  hasValue(): boolean;
  clearValue(): VideoMetaData;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VideoMetaData.AsObject;
  static toObject(includeInstance: boolean, msg: VideoMetaData): VideoMetaData.AsObject;
  static serializeBinaryToWriter(message: VideoMetaData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VideoMetaData;
  static deserializeBinaryFromReader(message: VideoMetaData, reader: jspb.BinaryReader): VideoMetaData;
}

export namespace VideoMetaData {
  export type AsObject = {
    value?: UUID.AsObject,
  }
}

export class UUID extends jspb.Message {
  getValue(): string;
  setValue(value: string): UUID;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UUID.AsObject;
  static toObject(includeInstance: boolean, msg: UUID): UUID.AsObject;
  static serializeBinaryToWriter(message: UUID, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UUID;
  static deserializeBinaryFromReader(message: UUID, reader: jspb.BinaryReader): UUID;
}

export namespace UUID {
  export type AsObject = {
    value: string,
  }
}

export class VideoFrames extends jspb.Message {
  getB64image(): string;
  setB64image(value: string): VideoFrames;

  getWidth(): number;
  setWidth(value: number): VideoFrames;

  getHeight(): number;
  setHeight(value: number): VideoFrames;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VideoFrames.AsObject;
  static toObject(includeInstance: boolean, msg: VideoFrames): VideoFrames.AsObject;
  static serializeBinaryToWriter(message: VideoFrames, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VideoFrames;
  static deserializeBinaryFromReader(message: VideoFrames, reader: jspb.BinaryReader): VideoFrames;
}

export namespace VideoFrames {
  export type AsObject = {
    b64image: string,
    width: number,
    height: number,
  }
}

