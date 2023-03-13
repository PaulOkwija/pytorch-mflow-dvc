import os 
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image


class CustomImageDataset(Dataset):
    def __init__(self, filepath_df, path, transform=None, target_transform=None):
        filepath_df = pd.read_csv('./data/external/Breast_cancer_dataset.csv')
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
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label

