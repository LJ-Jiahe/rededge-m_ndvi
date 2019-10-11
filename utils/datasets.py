import os

from torch.utils.data import Dataset
from PIL import Image

def sort_key(content_name):
    content_name_split = content_name.split('.')[0].split('_')
    return int(content_name_split[1]) + int(content_name_split[2])

class RedEdgeDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform

        self.content_dirs = os.listdir(data_dir).sort()
        self.content_dirs = [os.path.join(data_dir, content_dir) 
                            for content_dir in self.content_dirs]
        self.contents = []
        for content_dir in self.content_dirs:
            self.contents.append(os.listdir(os.path.join(content_dir)))

        self.contents.sort(key=sort_key)

    

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, idx):
        input_image = Image.open(os.path.join(self.data_dir,
                                              self.input_dir,
                                              self.input_contents[idx]))
        target_image = Image.open(os.path.join(self.data_dir,
                                               self.target_dir,
                                               self.target_contents[idx]))

        item = {'input_image': self.transform(input_image),
                'target_image': self.transform(target_image)}

        return item


# class Classification_Dataset(Dataset)
#     def __init__(self, data_dir, transform=None):
#         self.data_dir = data_dir
        
    
#     def __getitem__(self, idx):