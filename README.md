# RepXplorer - Bicep Curl Tracking Web App

## Description

RepXplorer is a web-based application designed to track and count bicep curls using a camera. Users can input the number of curls they plan to perform, and the application will provide real-time feedback on the number of curls detected.

## Features

- **Real-time Pose Detection:** Utilizes the MediaPipe Pose library for accurate real-time pose detection.
  
- **Web Interface:** Provides a user-friendly web interface where users can input the number of curls.

- **Dynamic Count Display:** Displays the count of both entered curls and detected curls on the web page.

## Files Included

- **app.py:** Main Python script containing the Flask application and camera-related logic.

- **camera.py:** Defines the `VideoCamera` class responsible for video capturing and pose detection.

- **index.html:** HTML template for the initial page with the form to enter the number of curls.

- **index3.html:** HTML template for the main tracking page displaying the video feed and curl count.

- **style3.css:** CSS stylesheet defining styles for the web pages.

## Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/that-ar-guy/bicep-curl-tracker.git

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Flask Application:**
   ```bash
   python app.py

4.**Access the Web App:**
Open your web browser and navigate to http://localhost:5000.

5.**Usage:**
  On the initial page (index.html), enter the number of curls you plan to perform.
  Press "Submit" to start the tracking.

6.**Stopping the Tracking:**
  Press "Q" on your keyboard to stop the tracking.

7.**Results:**
  The main tracking page (index3.html) will display the video feed on the left and the curl count on the right.

8.**Exiting:**
The application automatically stops tracking once the detected curl count matches the entered curl count.

9.**Dependencies:**<br>
Flask<br>
OpenCV<br>
NumPy<br>
MediaPipe<br>
