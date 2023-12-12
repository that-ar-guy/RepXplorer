from flask import Flask, render_template, request, redirect, url_for, Response
from flask_socketio import SocketIO
import cv2
from camera import VideoCamera  # Assuming the camera module is in a file named camera.py

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        exercise = request.form['exercise']
        if exercise == 'bicep_curls':
            return redirect(url_for('bicep_curls_page'))
        elif exercise == 'squats':
            return redirect(url_for('squats_page'))
    return render_template('landing.html')

@app.route('/bicep_curls', methods=['GET', 'POST'])
def bicep_curls_page():
    if request.method == 'POST':
        total_curls = int(request.form['total_curls'])
        return redirect(url_for('video_feed'))
    return render_template('bicep_curls.html')  # Replace 10 with the default number of curls
  # Replace 10 with the default number of curls

def gen(camera):
    while True:
        jpeg = camera.get_frame()
        if cv2.waitKey(1) & 0xFF == 27:
            break

        socketio.emit('update')

        yield (b'--frame\r\n'
               b'Content-type: image/jpeg\r\n\r\n' + jpeg
               + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    socketio.run(app, debug=True)
