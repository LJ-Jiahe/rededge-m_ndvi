
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.utils import save_image
from tqdm import tqdm
from matplotlib import pyplot as plt
import numpy as np
import torch

from utils import RedEdgeDataset, ndvi


# Initialize Dataset & Dataloader
dataset = RedEdgeDataset(data_dir="data/",
                         transform=transforms.ToTensor())
dataloader = DataLoader(dataset=dataset,
                        batch_size=1,
                        shuffle=False)

for ite, images in enumerate(tqdm(dataloader, desc="Saving images")):
    ndvi_value = ndvi(images)
    plt.figure()
    img = plt.imshow(ndvi_value)
    img.set_cmap('RdYlGn')
    plt.axis('off')
    plt.savefig("ndvi_matplotlib/"+str(ite)+".png", bbox_inches='tight')
    plt.close()
    # save_image(ndvi_value, "ndvi/"+str(ite)+".jpg")

