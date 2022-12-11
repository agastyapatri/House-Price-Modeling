import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os 
from src.dataset import Data
from src.model import RNN
import src.traintest 

"""
    Performing the steps for modeling
"""

#   1. Loading the data
dataset = Data(path="/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data/final_data.csv")
for i, (sample, target) in enumerate(dataset):
    print(sample) 
