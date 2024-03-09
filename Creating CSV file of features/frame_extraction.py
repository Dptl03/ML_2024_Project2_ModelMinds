import cv2
import os

def extract_frames(video_path, output_folder):

    cap = cv2.VideoCapture(video_path)
    

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    print(f"Total frames: {frame_count}, FPS: {fps}")

    for frame_number in range(frame_count):
        ret, frame = cap.read()

        if not ret:
            break

        frame_filename = f"frame_{frame_number:04d}.jpg"
        frame_path = os.path.join(output_folder, frame_filename)
        cv2.imwrite(frame_path, frame)

        print(f"Frame {frame_number}/{frame_count} saved: {frame_filename}")

    cap.release()

    print("Frames extraction complete.")

video_path = './Dataset/DJI_0024.mp4'
output_folder = './frames'

extract_frames(video_path, output_folder)