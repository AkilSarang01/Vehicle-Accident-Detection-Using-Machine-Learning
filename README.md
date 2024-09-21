# Vehicle Accident Detection Using Machine Learning

This project utilizes the **YOLOv8** model to detect vehicle accidents in real-time from video feeds, improving road safety by providing immediate alerts to authorities, which enables faster response times and data-driven insights for accident detection.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
  - [Clone the Repository](#1-clone-the-repository)
  - [Install Required Packages](#2-install-required-packages)
  - [Download the Dataset](#3-download-the-dataset)
- [Running the Application](#running-the-application)
- [Contact](#contact)
- [Contributions](#contributions)

## Overview

The **Vehicle Accident Detection** system is designed to analyze video footage and detect accidents in real time using machine learning techniques. It helps enhance safety and traffic management by offering timely notifications of accidents and valuable insights.

## Features
- Real-time accident detection
- YOLOv8 object detection model
- Output video with highlighted accidents
- Immediate alerts for faster response

## Dataset

Due to the large dataset size, it is hosted externally. You can download the dataset via [Google Drive](https://drive.google.com/file/d/1ILyEIC41Lo0sMR9ZiqkHCPtS8q5Fq2Ja/view?usp=drive_link).

## Installation

### 1. Clone the Repository

   ```bash
   git clone https://github.com/YOUR_USERNAME/vehicle-accident-detection.git
   cd vehicle-accident-detection
   ```

### 2. Install Required Packages

   Create a virtual environment and install the necessary dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   pip install -r requirements.txt
   ```

### 3. Download the Dataset

   Download the dataset using the provided Google Drive link and place it in the appropriate directory within the project.

## Running the Application

Run the detection system with the following command:

```bash
python detect.py --input video.mp4 --output output.mp4
```

- **Input:** Provide a video file of traffic footage.
- **Output:** The system will generate an output video with detected accidents highlighted.

## Contact

For queries or issues, please reach out via email: `sarangakil74@gmail.com`.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request for any enhancements or bug fixes.
