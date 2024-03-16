import cv2
import os

def frames_to_video(frames_folder, output_video_path, fps):
    frame_files = sorted(os.listdir(frames_folder))
    frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame_file in frame_files:
        print(frame_file)
        frame_path = os.path.join(frames_folder, frame_file)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)

    video_writer.release()

frames_folder = './bounddimg'  
output_video_path = 'output_video.mp4'  
fps = 30 

frames_to_video(frames_folder, output_video_path, fps)