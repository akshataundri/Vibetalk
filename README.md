# VibeTalk – AI-Powered Assistive Communication System  

VibeTalk is an AI-powered assistive communication system designed to bridge the communication gap between individuals with hearing and speech impairments and the general population. The system converts **Indian Sign Language (ISL)** gestures into **readable text and audible speech in real time**, promoting inclusivity, accessibility, and independence.

---

## Problem Statement
Individuals with hearing and speech impairments face major challenges in everyday communication because most people do not understand sign language. Existing solutions are often expensive, hardware-dependent, or require continuous internet connectivity.

VibeTalk addresses this gap by providing a **low-cost, web-based, offline assistive communication system** using computer vision and artificial intelligence.

---

## Features
- Real-time **Indian Sign Language (ISL) gesture recognition**
- Converts gestures into **text and speech**
- Uses **standard webcam** (no special hardware required)
- **Offline functionality** (no internet needed after setup)
- Simple and user-friendly web interface
- Supports **alphabet, number, and word recognition**
- Lightweight and cost-effective solution

---

## Technologies Used

### Programming & Frameworks
- **Python**
- **Flask** (Backend)
- **HTML & CSS** (Frontend)

### AI & Computer Vision
- **MediaPipe** – Hand landmark detection (21 points)
- **OpenCV** – Image processing
- **CNN-based gesture recognition model**

### Text-to-Speech
- **pyttsx3** – Offline text-to-speech synthesis

---

##  System Architecture
1. Webcam captures hand gestures
2. MediaPipe detects hand landmarks
3. AI model classifies gestures
4. Recognized gesture is converted into:
   - Text (displayed on UI)
   - Speech (audio output)

---

##  How to Run the Project

### Prerequisites
- Python 3.9+
- Webcam
- VS Code / PyCharm

### Install Dependencies
```bash
pip install opencv-python mediapipe flask pyttsx3 numpy pandas
