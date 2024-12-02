import cv2

video_path = "test.mp4"
output_folder = "images"
photos = 300

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = cap.get(cv2.CAP_PROP_FPS)

frames_to_extract = total_frames // photos

frame_count = 0
photo_count = 0

while cap.isOpened() and photo_count < photos:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frames_to_extract == 0:
        frame_name = f"{output_folder}/frame_{photo_count + 1:03d}.jpg"
        cv2.imwrite(frame_name, frame) 
        photo_count += 1
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
