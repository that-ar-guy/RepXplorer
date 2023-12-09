##RepXplorer - Bicep Curl Tracking Web App

#Description
RepXplorer is a web-based application designed to track and count bicep curls using a camera. Users can input the number of curls they plan to perform, and the application will provide real-time feedback on the number of curls detected.

#Features
Real-time Pose Detection: Utilizes the MediaPipe Pose library for accurate real-time pose detection.

Web Interface: Provides a user-friendly web interface where users can input the number of curls.

Dynamic Count Display: Displays the count of both entered curls and detected curls on the web page.

#Files Included
app.py: Main Python script containing the Flask application and camera-related logic.

camera.py: Defines the VideoCamera class responsible for video capturing and pose detection.

index.html: HTML template for the initial page with the form to enter the number of curls.

index3.html: HTML template for the main tracking page displaying the video feed and curl count.

style3.css: CSS stylesheet defining styles for the web pages.

#Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/RepXplorer.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask Application:

bash
Copy code
python app.py
Access the Web App:

Open your web browser and navigate to http://localhost:5000.

#Usage:

On the initial page (index.html), enter the number of curls you plan to perform.
Press "Submit" to start the tracking.
Stopping the Tracking:

Press "Q" on your keyboard to stop the tracking.
Results:

The main tracking page (index3.html) will display the video feed on the left and the curl count on the right.
Exiting:

The application automatically stops tracking once the detected curl count matches the entered curl count.

#Dependencies
Flask
OpenCV
NumPy
MediaPipe
