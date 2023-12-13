from flask import Flask, render_template, Response, request, redirect, url_for
from flask_socketio import SocketIO
from camera import VideoCamera
import cv2
from camera_squats import VideoCamera_S

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'bicep_curl':
            bicep_curls = request.form.get('bicep_curls')
            return redirect(url_for('bicep_curl', count=bicep_curls))
        elif form_type == 'squats':
            squats = request.form.get('squats')
            return redirect(url_for('squats', count=squats))
        else:
            return redirect(url_for('landing'))

@app.route('/bicep_curl/<count>')
def bicep_curl(count):
    return render_template('bicep_curls.html', count=count)

@app.route('/squats/<count>')
def squats(count):
    return render_template('squats.html', count=count)

def gen(camera, count):
    while True:
        jpeg, remaining_curls = camera.get_frame(count)
        if cv2.waitKey(1) & 0xFF == 27:
            break

        socketio.emit('update', {'remaining_curls': remaining_curls})

        yield (b'--frame\r\n'
               b'Content-type: image/jpeg\r\n\r\n' + jpeg
               + b'\r\n\r\n')


@app.route('/video_feed/<int:count>')
def video_feed(count):
    return Response(gen(VideoCamera(), count), mimetype='multipart/x-mixed-replace;boundary=frame')

@app.route('/video_feed_squats/<int:count>')
def video_feed_squats(count):
    return Response(gen_s(VideoCamera_S(),count), mimetype='multipart/x-mixed-replace;boundary=frame')

def gen_s(camera_squats, count):
    while True:
        jpeg, remaining_squats = camera_squats.get_frame_squats(count)
        if cv2.waitKey(1) & 0xFF == 27:
            break

        socketio.emit('update', {'remainremaining_squats':remaining_squats})

        yield (b'--frame\r\n'
               b'Content-type: image/jpeg\r\n\r\n' + jpeg
               + b'\r\n\r\n')
if __name__ == '__main__':
    app.run(debug=True)
