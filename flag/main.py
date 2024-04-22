
from ultralytics import YOLO
import cv2
prediction_model = YOLO("C:/Users/DELL/Downloads/flag/best.pt")
# Load a single image
image_path = "C:/Users/DELL/Downloads/flag/1.jpg"
frame = cv2.imread(image_path)

# Perform inference using the YOLO model
results = prediction_model(frame)

for result in results:
    boxes = result.boxes
    for box in boxes:
      conf = box.conf[0]
      cls = box.cls[0]
      x1, y1, x2, y2 = box.xyxy[0]
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(frame, f"Red Flag --> Conf: {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Resize the frame
resized_frame = cv2.resize(frame, (640, 420))  # Specify the new width and height

# Display the annotated and resized image
cv2.imshow("Detection", resized_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()



