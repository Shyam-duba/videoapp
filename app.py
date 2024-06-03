from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
cam = cv2.VideoCapture(0)

def home():
    while True:
        ret, frame = cam.read()

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
@app.route('/video_feed')
def video_feed():
    return Response(home(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





