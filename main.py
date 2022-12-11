"""
    Performing the steps for modeling
"""
import torch 
import torch.nn as nn 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os 
from src.dataset import Data
from src.model import RNN
from src.traintest import Trainer 


#   1. Loading the data
dataset = Data(path="/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data/final_data.csv")
dataloader = torch.utils.data.DataLoader(dataset, batch_size = 1, shuffle=False)

#   2. Defining the model and hyperparameters
model = RNN(input_dim = 7, hidden_dim = 32,  num_layers = 2,  output_dim = 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.01)


#   3. Enabling the training of the model on the created data. 
trainer = Trainer(num_epochs=100, lr=0.01)