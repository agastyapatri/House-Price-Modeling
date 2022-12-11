"""
    Python class to load the data. 
"""
import pandas as pd 
import numpy as np 
import os  
import torch 
import torch.nn as nn
import matplotlib.pyplot as plt


class Data(torch.utils.data.Dataset):
    """
        Creating a pytorch custom dataset returning a tuple of data, and target value. 
    """
    def __init__(self, path) -> None:
        super().__init__()
        self.landmarks = pd.read_csv(path, parse_dates=["DATE"], index_col=["DATE"])
    
    def __len__(self):
        #   returning the number of data samples
        return len(self.landmarks)

    def __str__(self):
        return f"\nDataset for the features affecting the S&P Case-Shiller Home Price Index.\nNumber of samples: {len(self.landmarks)}"

    def __getitem__(self, idx):
        #   returning the data sample at index i 
        vector = np.array(self.landmarks.iloc[idx, :].values, dtype=np.float32)
        tensor = torch.from_numpy(vector)[1:]
        target = torch.from_numpy(vector)[0]
        return tensor, target 

if __name__ == "__main__":
    PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data/final_data.csv"
    tensordata = Data(path = PATH)

    
    