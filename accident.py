import cv2
import requests
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('i1-yolov8s.pt')

# Open the video file
video_path = "./car-crash.mov"
cap = cv2.VideoCapture(video_path)

# Initialize a frame counter
frame_count = 0

# Define the function to send cropped images to the server
def send_cropped_image(image_path):
    url = "http://localhost:3000/upload"  # Replace with your server endpoint
    files = {'file': ('image.jpg', open(image_path, 'rb'), 'image/jpeg')}
    response = requests.post(url, files=files)
    print(response.text)  # Print the server response

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Check if any detections are present
        if len(results[0].boxes) > 0:
            # Increment the frame counter
            frame_count += 1

            # Save the frame when an object is detected
            save_path = f"./img/frame_{frame_count}.jpg"
            cv2.imwrite(save_path, frame)

            # Send the cropped image to the server
            send_cropped_image(save_path)
            print(f"Frame {frame_count} saved and sent.")

        # Break the loop if 'q' is pressed

    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
