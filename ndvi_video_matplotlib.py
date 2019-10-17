import os

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
from PIL import Image
from tqdm import tqdm

import config as cfg


image_list = [img for img in cfg.ndvi_image_dir_colored 
              if img.endswith(cfg.image_extension)]
image_list.sort(key=lambda x: int(x.split('.')[0]))
image_list = [os.path.join(cfg.ndvi_image_dir_colored, content_dir) 
              for content_dir in image_list]
image_list = image_list[cfg.image_range]

frames = []
fig = plt.figure()
for im in tqdm(image_list):
    image = Image.open(im)
    frames.append([plt.imshow(image, animated=True)])

ani = animation.ArtistAnimation(fig=fig, 
                                artists=frames, 
                                interval=100, 
                                repeat_delay=100, 
                                blit=True)
ani.save('ndvi.mp4')
plt.show()