from flask import Flask, render_template, Response, request, redirect, url_for
from flask_socketio import SocketIO
from camera import VideoCamera
import cv2

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        curls = request.form['curlCount']
        return redirect(url_for('base', curls=curls))
    return render_template('index.html')

def gen(camera):
    while True:
        jpeg, rep_count = camera.get_frame()
        if cv2.waitKey(1) & 0xFF == 27:
            break

        socketio.emit('update', {'rep_count': rep_count})


        yield (b'--frame\r\n'
               b'Content-type: image/jpeg\r\n\r\n' + jpeg
               + b'\r\n\r\n')

@app.route('/base')
def base():
    curls = request.args.get('curls', '')
    return render_template('index3.html', curls=curls)

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    socketio.run(app, debug=True)
