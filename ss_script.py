import subprocess, cv2

def capture_screen():
    subprocess.run("adb exec-out screencap -p > screen.png", shell=True)
    return "screen.png"

img = cv2.imread("screen.png")

img_resized = cv2.resize(img, (128, 128))

img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

img_normalized = img_gray / 255.0

import torch
img_tensor = torch.tensor(img_normalized, dtype=torch.float32).unsqueeze(0)