# Real-Time Object Tracker

## Overview
This project implements a real-time object tracking system using a live webcam feed. The user can select an object in the first frame using a bounding box, and the system will track the selected object as it moves within the video feed.

## Features
- Allows user to manually select an object in the first frame.
- Tracks the selected object in real-time.
- Displays tracking results in a live video feed.
- Saves the output as a video file (`output.avi`).

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install -r requirments.txt
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/AhmedSheded/Eyego_task.git
cd Eyego_task
```
2. Run the tracker script:
```bash
python tracker.py
```
3. Select the object in the first frame by drawing a bounding box and pressing `SPACE` or `ENTER`.
4. The system will track the selected object in real-time.
5. Press `q` to exit the program.

## Implementation Details
The tracking system uses OpenCV's built-in `cv2.TrackerCSRT_create()` algorithm. The workflow involves:
1. Capturing video frames from the webcam.
2. Allowing user input for object selection.
3. Applying a tracking algorithm to follow the selected object.
4. Updating the bounding box in each frame and displaying results.
5. Saving the tracking output to `output.avi`.

## Demo
![Tracking Demo](https://raw.githubusercontent.com/ahmedsheded/Eyego_task/main/assets/output.gif)


## Deployment Instructions
- Ensure all dependencies are installed.
- Run the script and follow the on-screen instructions to select and track an object.

## Contributing
If you have suggestions or improvements, feel free to open a pull request.

## License
This project is open-source and available under the MIT License.

---
For any inquiries, contact: t.senosy@eyego.ai

