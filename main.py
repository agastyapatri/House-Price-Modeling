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


PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/"

#   1. Loading the data
dataset = Data(path=os.path.join(PATH, "data/final_data.csv"))       
dataloader = torch.utils.data.DataLoader(dataset, batch_size = 1, shuffle=False)
 

#   2. Defining the LSTM network
network = RNN(input_dim = 7, hidden_dim = 24,  num_layers = 20,  output_dim = 1)

#   3. Conducting the training process
trainer = Trainer(model = network, dataloader=dataloader, num_epochs=50, lr=0.0001)


trained_network = network.load_state_dict(torch.load(os.path.join(PATH, "figures-results/saved_network.pth")))
