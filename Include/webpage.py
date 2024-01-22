from flask import Response
from flask import Flask
from flask import render_template
from Include import webcam

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

def gen_frames(webcam: webcam.Camera):
    while True:
        frame = webcam.capture_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame
            + b'\r\n\r\n')

@app.route('/webcam_ip')
def webcam_ip():
    return Response(gen_frames(webcam.Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


class Page(object):
    def __init__(self):
        self.__app = app
        self.__app.run(host='0.0.0.0', port=1234, debug=True)
