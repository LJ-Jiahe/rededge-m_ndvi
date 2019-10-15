import os

from torch.utils.data import Dataset
from PIL import Image
import numpy as np

from .functions import sort_key


class RedEdgeDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.band_names = ["blue", "green", "red", "near_ir", "red_edge"]
        self.data_dir = data_dir
        self.transform = transform

        self.content_dirs = os.listdir(data_dir)
        self.content_dirs.sort()
        self.content_dirs = [os.path.join(data_dir, content_dir) 
                            for content_dir in self.content_dirs]
        self.contents = []
        for content_dir in self.content_dirs:
            current_contents = os.listdir(content_dir)
            current_contents = [os.path.join(content_dir, current_content) for current_content in current_contents]
            self.contents += current_contents

        self.contents.sort(key=sort_key)
        self.contents = np.reshape(self.contents, (-1, 5))

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, idx):
        images = dict()
        for ite, content in enumerate(self.contents[idx]):
            image = Image.open(content)
            images[self.band_names[ite]] = self.transform(image)
        return images
