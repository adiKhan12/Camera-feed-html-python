import cv2

# Define the webcam video capture object
cap = cv2.VideoCapture(0)

# Loop to continuously capture frames from the webcam
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()