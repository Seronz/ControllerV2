import cv2
import subprocess

# Membaca aliran video dari perangkat Android melalui ADB
command = f'adb shell "dumpsys media.camera" | grep -A 1 "Camera ID 0" | tail -n 1 | cut -d ":" -f 2 | sed -e "s/^ *//g"'
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, _ = proc.communicate()
camera_id = output.strip()

cap = cv2.VideoCapture(f'adb shell "service call media.camera {camera_id} s16 android.frameworks.surfacetexture.ISurfaceTexture.getBuffer"')
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Tampilkan frame
    cv2.imshow('Android Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
