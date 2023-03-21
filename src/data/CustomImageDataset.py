import os 
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image
import yaml


class CustomImageDataset(Dataset):
    def __init__(self,csv_path, path, transform=None, target_transform=None):
        filepath_df = pd.read_csv(csv_path)
        self.img_labels = filepath_df['class']
        self.img_name = filepath_df['images']
        self.transform = transform
        self.path = path
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.path, self.img_name[idx])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx]
        label_map = yaml.safe_load(open('./data/processed/labels_map.yaml'))
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        ind = list(label_map.values()).index(label)
        return image, list(label_map.keys())[ind]

