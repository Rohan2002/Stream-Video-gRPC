# Video Streaming Project with gRPC API.

# gRPC
gRPC is an Remote Procedure Call System. It is particularly useful for micro-services based archietecture platforms. Suppose we have multiple micro services implemented in different languages like C++, Python, NodeJS, and multiple clients implemented in Android-java, Ruby, React-Javascript. Then gRPC will ease the service-client communication by transfering messages through Google's language and platform neutral serialized data structure called Protobuf. Since gRPC uses protobuf to communicate between the client and services, it is also efficient in comparison with communication through JSON or XML because protobuf allows its data to be serialized and deserialized when needed.

# Technologies used so far.
Python, OpenCV, gRPC, Protobufs, Threading.

# Project
Video streaming is an example of server-streaming rpc and that is one of the 4 paradigms of gRPC API. 
The server-streaming RPC is similar to a unary RPC, except that the server returns a stream of messages in response to a client’s request. 
In our example, the client will send a single ping (video uuid), and the server will return return a stream of pongs (video frames).

I also added threads to make video streaming faster on the client side. One thread reads the frame from the given video and puts it in a 
queue, and then the second thread sends the frames to the client by reading the frames from the queue at constant rate that is dependent
based on the given video's FPS.

# Future
1. Integrate this video-streamer on HTTP Protocol. 
2. Create a client in React to play video files.

# Steps to run the current program without Docker.
1. Git clone this repo.
2. Run ```pip3 -r install requirements.txt```
3. Then open two terminal windows(one for client, and one for server).
4. Then run ```make run-client``` and ```make run-server``` on the respective terminals.

# Steps to run the current program on Docker. ( In progress, still figuring out how to run GUI apps on Docker)
1. ```docker-compose build```
2. ```docker-compose up```


# Picture of Demo
![demo_plot](./demo.png)
# Author
Rohan Deshpande