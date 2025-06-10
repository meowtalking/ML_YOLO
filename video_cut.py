import supervision as sv
import cv2
import os

SOURCE_VIDEO_PATH = "/Users/macbook/Desktop/иц бт/задание 5/ГТ-219_1_Камера_219_ГТ-219_1_Камера_219_17.09.2024_17.30.00-17.09.2024_17.45.00.mp4"
TARGET_DIR = "/Users/macbook/Desktop/иц бт/задание 5/нарезанные изображения"

EVERY_X_FRAME = 300

cap = cv2.VideoCapture(SOURCE_VIDEO_PATH)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % EVERY_X_FRAME == 0:
        frame_filename = os.path.join(TARGET_DIR, f"frame_{frame_count:06d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")

    frame_count += 1

cap.release()
print(f"Ready!! Total frames processed: {frame_count}, frames saved: {frame_count // EVERY_X_FRAME}")