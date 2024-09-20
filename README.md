# Vehicle-Accident-Detection-Using-Machine-Learning
This project utilizes YOLOv8 to detect vehicle accidents in real-time from video feeds. It enhances road safety by providing immediate alerts to authorities, enabling faster response times and data-driven insights for accident detection.

Overview
This project implements a vehicle accident detection system using machine learning techniques, specifically the YOLO v8 object detection model. The system is designed to analyze video footage and detect accidents in real time, providing valuable insights for safety and traffic management.

Dataset
Due to the large size of the dataset used for training and evaluation, it cannot be uploaded directly to this repository. However, you can access the dataset via the following Google Drive link:

Download Dataset:-https://drive.google.com/file/d/1ILyEIC41Lo0sMR9ZiqkHCPtS8q5Fq2Ja/view?usp=drive_link

Installation
To set up the project, follow these steps:

Clone the Repository

bash
Copy code
git clone https://github.com/YOUR_USERNAME/vehicle-accident-detection.git
cd vehicle-accident-detection
Install Required Packages Create a virtual environment and install the necessary dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Download the Dataset Access the dataset using the link provided above and place it in the appropriate directory within the project.

Run the Application Use the following command to start the detection system:

bash
Copy code
python detect.py --input video.mp4 --output output.mp4

Usage
Input: Provide a video file of traffic footage.
Output: The system will generate an output video with detected accidents highlighted.
Contact
For any queries or issues, please reach out to:

Email: sarangakil74@gmail.com
Contributions
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
