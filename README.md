# 🖐️ Real-Time Finger Counter

This project utilizes your computer's webcam to detect your hand and count the number of fingers shown in real-time using **OpenCV**, **MediaPipe**, and **NumPy**.

## 🚀 Getting Started

### Prerequisites
* Python 3.9 or higher installed.

### Installation

1.  (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows: .venv\Scripts\activate
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

Run the main script to start the camera:
``bash
python src/finger_counter.py

## 🧠 How It Works
Detection: The MediaPipe Hands model extracts the palm orientation and identifies 21 distinct hand landmarks.

Analysis: The algorithm analyzes the coordinates of finger knuckles relative to the palm to determine if each finger is in an "open" or "closed" state.

Output: The total count of open fingers and the current FPS (Frames Per Second) are displayed on the screen.

### 💡 Tips for Best Results
Lighting: Use the application in a well-lit environment for better detection accuracy.

Positioning: Keep your hand parallel to the camera and ensure all fingers are visible within the frame.

Single Hand: The algorithm is optimized for a single hand; if multiple hands are present, it will track the first detected hand.

### 📄 License
This project is licensed under the MIT License.

### by vira
