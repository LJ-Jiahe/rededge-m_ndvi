import os

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
from PIL import Image
from tqdm import tqdm


image_list = [img for img in os.listdir("ndvi/") if img.endswith(".png")]
image_list.sort(key=lambda x: int(x.split('.')[0]))
image_list = [os.path.join("ndvi/", content_dir) for content_dir in image_list]
image_list = image_list[200:250]

frames = [] # for storing the generated images
fig = plt.figure()
for im in tqdm(image_list):
    image = Image.open(im)
    frames.append([plt.imshow(image, animated=True)])

ani = animation.ArtistAnimation(fig, frames, interval=100, repeat_delay=100, blit=True)
ani.save('ndvi.mp4')
plt.show()