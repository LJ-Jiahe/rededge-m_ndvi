import os

import cv2
from tqdm import tqdm

import config as cfg


image_folder = cfg.ndvi_image_dir_colored

images = [img for img in os.listdir(image_folder) 
          if img.endswith(cfg.image_extension)]
images.sort(key=lambda x: int(x.split('.')[0]))
images = images[cfg.image_range]

height, width, layers = cv2.imread(os.path.join(image_folder, images[0])).shape
video = cv2.VideoWriter(filename=cfg.video_name, 
                        fourcc=0, 
                        fps=10, 
                        frameSize=(width,height))

for image in tqdm(images):
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()