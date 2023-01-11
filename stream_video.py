from flask import Flask, Response
import cv2

# Create the Flask app
app = Flask(__name__)

# Define the webcam video capture object
cap = cv2.VideoCapture(0)

# Define the function to generate the video frames
def generate():
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame)

        # Return the current frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

# Define the video feed route
@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
