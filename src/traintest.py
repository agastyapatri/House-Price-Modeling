"""
    Training the model
"""
import numpy as np 
import torch 
import torch.nn as nn 
from model import RNN
from dataset import Data

class Trainer(nn.Module):
    def __init__(self, num_epochs, lr, ):
        super().__init__()
        self.num_epochs = num_epochs
        self.lr = lr 
        self.trained_model = self.train_all_epochs()
    
    def train_one_epoch(self, model):
        #   Function to iterate over the dataset
        pass 
    
    def train_all_epochs(self):
        #   Function to iterate over all the epochs
        pass 


if __name__ == "__main__":
    dataset = Data(path="/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data/final_data.csv")   
    dataloader = torch.utils.data.DataLoader(dataset, batch_size = 1, shuffle=False)
    network = RNN(input_dim = 7, hidden_dim = 1,  num_layers = 2,  output_dim = 1)

    for i, data in enumerate(dataloader):
        sample, target = data 
        sample = sample.unsqueeze(0)
        output = network(sample)
        print(output)
        break 
 
