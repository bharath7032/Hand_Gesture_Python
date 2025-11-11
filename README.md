# Hand Gesture Recognition using OpenCV & MediaPipe

## Overview
This project uses **OpenCV** and **MediaPipe** to detect and recognize hand gestures from a webcam feed in real time.  
It counts the number of raised fingers and maps them to simple control commands like **MOVE FORWARD**, **TURN LEFT**, or **STOP**.

---

## Features
- Real-time hand tracking using **MediaPipe Hands**
- Finger counting logic for one hand (0–5 fingers)
- Displays live video with hand landmarks drawn
- Shows corresponding **command text** on the screen
- Prints detected command in the console
- Easy to extend for gesture-controlled robots or games

---

## How It Works
1. Captures video from the webcam using **OpenCV**  
2. Detects hand landmarks using **MediaPipe**
3. Counts the number of raised fingers:
   - Index, Middle, Ring, and Little fingers: based on Y-coordinate of landmarks  
   - Thumb: based on X-coordinate
4. Maps the finger count to a specific command:
   | Fingers Raised | Command        |
   |----------------|----------------|
   | 0              | STOP           |
   | 1              | MOVE FORWARD   |
   | 2              | MOVE BACKWARD  |
   | 3              | TURN LEFT      |
   | 4              | TURN RIGHT     |
   | 5              | READY          |
5. Displays the command on the screen and console

---

## Installation

### 1. Clone or download the project
```bash
git clone https://github.com/bharath7032/Hand_Gesture_Python.git
cd Hand_Gesture_Python

```

### 2. Install dependencies
```bash
pip install opencv-python mediapipe
```

### 3. Run the project
```bash
python handproject.py
```

---

## Requirements
- Python 3.8+
- OpenCV (`cv2`)
- MediaPipe
- Webcam

---

##  Output Example
When you raise:
- 1 finger → `MOVE FORWARD` appears on the video window  
- 5 fingers → `READY`  
- 0 fingers → `STOP`

---

## File Structure
```
handproject.py        # Main program file
README.md             # Project documentation
```

---

## Future Enhancements
- Add gesture-based robot control via serial communication
- Support for dual-hand gesture detection
- Integrate sound or speech output for commands
- Include gesture-based game controls

---

