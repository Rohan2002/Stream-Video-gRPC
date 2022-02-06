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
    def __init__(self, video:Path) -> None:

        self.video=video
        self.activate = False

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
        self.frame_reader_thread.start()

        if self.cap.isOpened():
            logging.info(f"Frame sender thread started. Video has {self.fps} fps!")

        self.frame_sender_thread.start()
    
    def release_video_resources(self):
        """
            Join threads, and release resources
        """
        self.frame_reader_thread.join()
        self.frame_sender_thread.join()
        
        self.cap.release()

    def read_frame(self):
        """
            Put all frames in the queue.
        """
        while self.activate:
            status, frame = self.cap.read()
            if status:
                logging.info("Putting frames...")
                self.frame_queue.put(frame)
            else:
                if self.frame_queue.empty():
                    self.activate = False
                else:
                    continue
    
    def preprocess_frame(self, frame: np.ndarray):
        """
            Preprocess frames before sending them to client.
        """
        _, buffer = cv.imencode('.png', frame)
        return base64.b64encode(buffer).decode('utf-8')

    def send_frame(self):
        """
            Send frames to client at a constant rate.
        """
        frm = current_timer = None
        while self.activate:
            # get most recent frame
            while not self.frame_queue.empty():
                frm = self.frame_queue.get_nowait()
                if frm is not None:
                    if current_timer is None:
                        current_timer = time.perf_counter()

                    encoded_preprocessed_frame = self.preprocess_frame(frm)
                    logging.info(f"Sending frames...{self.num_frames}")
                    yield (encoded_preprocessed_frame, frm.shape)
                    self.num_frames += 1
                dt = (
                    self.dt
                    if current_timer is None
                    else max(0, current_timer + self.num_frames * self.dt - time.perf_counter())
                )
                time.sleep(dt)

