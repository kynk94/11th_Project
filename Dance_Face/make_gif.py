import numpy as np
import matplotlib.pyplot as plt
import cv2
from pathlib import Path
from skimage import io

import matplotlib.animation as ani
from IPython.display import HTML
import matplotlib

landmark_3D_dir = Path("./data/train/landmark/label")
landmark_3D_img_paths = sorted(landmark_3D_dir.iterdir())
# source_dir = Path('./data/source/test_img')
# target_dir = Path('./results/target/test_latest/images')
# label_dir = Path('./data/source/test_label_ori')
#
# source_img_paths = sorted(source_dir.iterdir())
# target_synth_paths = sorted(target_dir.glob('*synthesized*'))
# target_label_paths = sorted(label_dir.iterdir())


def animate(nframe):
    ax1.clear()

    landmark_3D_img = io.imread(landmark_3D_img_paths[nframe])
    ax1.imshow(landmark_3D_img)
    ax1.set_xticks([])
    ax1.set_yticks([])

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(111)

anim = ani.FuncAnimation(fig, animate, frames=len(landmark_3D_img_paths), interval=1000 / 24)
plt.close()

js_anim = HTML(anim.to_jshtml())

anim.save("label.gif", writer="imagemagick")
