"""
    Core functionality to stream videos.
    Use send_frames as this is a generator that will yield a base64 encoded frame.
    @author: Rohan Deshpande
"""
import logging
import queue
import logging
import cv2 as cv
import numpy as np
import base64
import time
from threading import Thread
from pathlib import Path

class VideoStreamer:
    def __init__(self, video:Path, html:bool) -> None:

        self.video=video
        self.activate = False
        self.html = html
    def init_video(self):
        """
            Init video threads, and open-cv stuff.
        """
        if not self.video.exists():
            raise FileNotFoundError(f"Couldn't locate video file {self.video}")
        
        # Read frame with this thread
        self.frame_reader_thread = Thread(target=self.read_frame, args=(), name="reader")
        self.frame_reader_thread.daemon = True

        # Send frames with this thread.
        self.frame_sender_thread = Thread(target=self.send_frame, args=(), name="sender")
        self.frame_sender_thread.daemon = True

        # Frame queue
        self.frame_queue = queue.Queue()

        self.cap = cv.VideoCapture(str(self.video))
        
        self.fps = self.cap.get(cv.CAP_PROP_FPS)
        self.dt = 1./self.fps
        self.num_frames = 0

        self.start_video()
    
    def start_video(self):
        """
            Start threads
        """
        self.activate = True
        logging.info("Starting Reader Thread....")
        self.frame_reader_thread.start()

        if self.cap.isOpened():
            logging.info(f"Reader thread started. Video has {self.fps} fps!....")

        logging.info("Starting Sender Thread....")
        self.frame_sender_thread.start()
        
    
    def release_video_resources(self):
        """
            Join threads, and release resources
        """
        self.activate = False
        
        if (self.frame_reader_thread.is_alive()):
            logging.info("Joining Reader Thread....")
            self.frame_reader_thread.join()
        
        if (self.frame_sender_thread.is_alive()):
            logging.info("Joining Sender Thread....")
            self.frame_sender_thread.join()
        
        if self.cap.isOpened():
            logging.info("Releasing OpenCV Capture Resource....")
            self.cap.release()

    def read_frame(self):
        """
            Put all frames in the queue.
        """
        while self.activate:
            status, frame = self.cap.read()
            if status:
                logging.info("Reading frames...")
                self.frame_queue.put((frame, status))
    
    def preprocess_frame(self, frame: np.ndarray):
        """
            Preprocess frames before sending them to client.
        """
        if self.html:
            _, buffer = cv.imencode('.png', frame)
            return base64.b64encode(buffer).decode('utf-8')
        else:
            return base64.b64encode(frame)

    def send_frame(self):
        """
            Send frames to client at a constant rate.
        """
        frm = current_timer = None
            # get most recent frame
        while self.activate:
            at_least_one_frame_read = False
            while not self.frame_queue.empty():
                frame, status = self.frame_queue.get_nowait()
                at_least_one_frame_read = status
                if frame is not None:
                    if current_timer is None:
                        current_timer = time.perf_counter()

                    encoded_preprocessed_frame = self.preprocess_frame(frame)
                    logging.info(f"Writing frames...{self.num_frames}")
                    yield (encoded_preprocessed_frame, frame.shape, True)
                    self.num_frames += 1
                dt = (
                    self.dt
                    if current_timer is None
                    else max(0, current_timer + self.num_frames * self.dt - time.perf_counter())
                )
                time.sleep(dt)
            
            if self.frame_queue.empty() and at_least_one_frame_read:
                logging.info("Sending signal to server about frame over.")
                yield ("", (0,0,0), False)