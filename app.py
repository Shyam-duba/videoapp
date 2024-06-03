from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
cam = cv2.VideoCapture(0)


@app.route('/')
def home():
    while True:
        ret, faces = cam.read()

        cv2.imshow("window", faces)

        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)





