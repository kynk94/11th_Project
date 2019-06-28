import numpy as np
import matplotlib.pyplot as plt
import cv2
from pathlib import Path
from skimage import io
import os
import matplotlib.animation as ani
from IPython.display import HTML
import matplotlib

landmark_dir = Path("./data/train/landmark")

want = "label"

want_dir = landmark_dir.joinpath(want)
want_img_paths = sorted(want_dir.iterdir())

gif_dir = Path("./gif")
gif_dir.mkdir(exist_ok=True)

def animate(nframe, img_paths=want_img_paths):
    ax1.clear()

    img = io.imread(img_paths[nframe])
    ax1.imshow(img)
    ax1.set_xticks([])
    ax1.set_yticks([])

fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(111)

anim = ani.FuncAnimation(fig, animate, frames=len(want_img_paths), interval=1000 / 24)
plt.close()

js_anim = HTML(anim.to_jshtml())

anim.save(gif_dir.joinpath(want+".gif"), writer="imagemagick")
if "None0000000.png" in os.listdir():
    os.remove("None0000000.png")