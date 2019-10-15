
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.utils import save_image
from tqdm import tqdm
from matplotlib import pyplot as plt

from utils import RedEdgeDataset, ndvi


# Initialize Dataset & Dataloader
dataset = RedEdgeDataset(data_dir="data/",
                         transform=transforms.ToTensor())
dataloader = DataLoader(dataset=dataset,
                        batch_size=1,
                        shuffle=False)

for ite, images in enumerate(tqdm(dataloader, desc="Saving images")):
    ndvi_value = ndvi(images)[0]
    # save_image(ndvi_value, "ndvi/"+str(ite)+".png")
    ndvi_value = ndvi_value[0]
    print(ndvi_value.min())
    print(ndvi_value.max())
    plt.imsave("ndvi/"+str(ite)+".png", ndvi_value, cmap=None)

