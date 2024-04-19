## Face Detection Program
This is a simple Python program that uses OpenCV to perform face detection on images captured from a camera feed. It uses the Haar Cascade classifier for detecting frontal faces.

## Installation
Before running the program, you need to install the required libraries. You can install them using the following command: pip install opencv-python

## Usage
1. Clone or download this repository to your local machine.
2. Make sure you have a camera available (built-in or external).
3. Run the face_detection.py script using Python. "python face_detection.py"
4. The program will open a window showing the camera feed with detected faces outlined by rectangles.

## Error Explanation
If you encounter the following error while running the program:
[ERROR:0@0.060] global persistence.cpp:505 cv::FileStorage::Impl::open Can't open file: 'haarcascade_frontalface_default.xml' in read mode
Traceback (most recent call last):
  File "face_detection.py", line 17, in <module>
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
cv2.error: OpenCV(4.7.0) ... modules\objdetect\src\cascadedetect.cpp:1689: error: (-215:Assertion failed) !empty() in function 'cv::CascadeClassifier::detectMultiScale'

This error occurs due to the program's inability to locate the 'haarcascade_frontalface_default.xml' file, which is required for the Haar Cascade face detection. Make sure that the XML file is present in the same directory as the script or provide the correct path to the CascadeClassifier initialization.

You can download the 'haarcascade_frontalface_default.xml' file from the OpenCV GitHub repository: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Place the downloaded XML file in the same directory as your script or provide the correct path in the CascadeClassifier initialization:
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')
