import os

# Define the path to the directory
img_directory = "C:\\Users\\91932\\computervision\\VAD final\\yolov8\\img"

# Check if the directory exists
if os.path.exists(img_directory):
    # Get a list of all files in the directory
    files = os.listdir(img_directory)
    
    # Iterate through the files and remove them
    for file_name in files:
        file_path = os.path.join(img_directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


uploads_directory = "C:\\Users\\91932\\computervision\\VAD final\\backend\\uploads"

# Check if the directory exists
if os.path.exists(uploads_directory):
    # Get a list of all files in the directory
    files = os.listdir(uploads_directory)
    
    # Iterate through the files and remove them
    for file_name in files:
        file_path = os.path.join(uploads_directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

# from ultralytics import YOLO
# import cv2

# model = YOLO('i1-yolov8s.pt')

# video_path = "car-crash.mov"

# results = model.predict(source="car-crash.mov",project="C:\Users\91932\computervision\VAD final\yolov8",name="img",save_crop=True)









