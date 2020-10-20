import cv2

cap = cv2.VideoCapture('output.mp4')

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()