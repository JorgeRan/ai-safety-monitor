import cv2
from ultralytics import solutions

address = "http://192.168.2.39:8080/video"
cap = cv2.VideoCapture(address)

if not cap.isOpened():
    raise RuntimeError("Error opening camera stream")

fps = 20
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_writer = cv2.VideoWriter(
    "security_output.avi",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

securityalarm = solutions.SecurityAlarm(
    show=True,
    model="yolo26n.pt",
    records=1,
)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Stream ended or frame failed")
        break

    results = securityalarm(frame)
    annotated = results.plot_im
    video_writer.write(annotated)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
