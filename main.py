from navigation import BasicNavigation
from model import Model_Run
import cv2
import time


def main():
    nav = BasicNavigation()
    model = Model_Run()  

    cap = cv2.VideoCapture("http://192.168.4.1:81/stream")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Camera read error")
                continue

            # Run your model on the camera frame
            label, confidence = model.classify_frame(frame)

            print(f"[Camera] {label} ({confidence:.2f})")

            if label == "stop" and confidence > 0.7:
                print("STOP detected → stopping motors")
                nav.stop()
            else:
                nav.go_straight()

            time.sleep(0.02)

    except KeyboardInterrupt:
        nav.stop()
        cap.release()
        print("Stopped by user.")


if __name__ == "__main__":
    main()
