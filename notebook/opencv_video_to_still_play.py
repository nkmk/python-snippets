import cv2
import os


def save_frame_play(video_path, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return
    
    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)
    
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow(window_name, frame)
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('c'):
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            elif key == ord('q'):
                break
            n += 1
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            n = 0
    
    cv2.destroyWindow(window_name)


save_frame_play('data/temp/sample_video.mp4', 'data/temp', 'sample_video_cap', delay=0)
