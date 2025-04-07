import cv2
# OpenCV

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    # Video capture to initialize the frames
    frames = []
    while True: # loop then it reads the frame
        ret, frame = cap.read() # it returns a flag whether there is a frame or the video has ended
        if not ret: # if it is false means that the video has ended and it will go out of the loop but if it's true, it will append the frame to the list of frame and then return it finally
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # the output format will be XVID
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) 
    # takes in video path and that's a string and then output video type 
    # 24 is the number of frames per second
    # in the () is the frame width and the frame height
    for frame in output_video_frames: # loop over each frame
        out.write(frame) # write the frame to the video writer
    out.release()