import cv2
from PIL import Image, ExifTags
import sys, traceback, argparse

def get_frames(file):
    cap = cv2.VideoCapture(file)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Over")
            break
        gray_fr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(Image.fromarray(gray_fr)) 
    print(frames)
    
    




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video to ascii art")
    parser.add_argument("-file", "-f", required=True)
    args = parser.parse_args()
    get_frames(args.file)