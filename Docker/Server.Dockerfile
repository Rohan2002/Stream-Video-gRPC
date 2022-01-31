FROM python:3.8

RUN adduser -u 1001 grpc-user

WORKDIR /app

RUN apt-get update && apt-get install -y \
        make \
        ffmpeg \
        libsm6 \
        libxext6 \
        && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./Makefile /app/Makefile
COPY vidservice/back_end /app/vidservice/back_end
COPY vidservice/protos /app/vidservice/protos
COPY vidservice/videos /app/vidservice/videos
RUN chown grpc-user:grpc-user /app

USER grpc-user
ENV PATH "/home/grpc-user/.local/bin:$PATH"

EXPOSE 50051