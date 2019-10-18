import torch
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from tqdm import tqdm
from matplotlib import pyplot as plt
import numpy as np

from utils import RedEdgeDataset, ndvi
import config as cfg


# Initialize Dataset & Dataloader
dataset = RedEdgeDataset(data_dir=cfg.data_dir,
                         transform=cfg.transform)
dataloader = DataLoader(dataset=dataset)

# Calculate ndvi for every camera position, and save to images.
# To save as colored image rather than grayscale, a matplotlib figure plot is 
# generated and then saved. The original grayscale image is saved, too.
for ite, images in enumerate(tqdm(dataloader, desc="Saving images")):
    # Calculate ndvi
    ndvi_value = ndvi(images)

    # Saving colored image
    plt.figure(frameon=False)
    img = plt.imshow(ndvi_value)
    img.set_cmap(cfg.colormap)
    plt.axis('off')
    plt.savefig(fname=cfg.ndvi_image_dir_colored + str(ite) + cfg.image_extension, 
                bbox_inches='tight',
                pad_inches=0,
                dpi=300)
    plt.close()
    
    # Saving grayscale image
    save_image(tensor=ndvi_value, 
               filename=cfg.ndvi_image_dir_grayscale + str(ite) + cfg.image_extension)
