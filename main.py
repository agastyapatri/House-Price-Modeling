import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from src.dataloader import Data
import os 
"""
    Performing the steps for modeling
"""
PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"
files = os.listdir(PATH)
series = [] 

for file in files: 
    try:
        df = pd.read_csv(os.path.join(PATH, file))
        series.append(df)
    except:
        print(file)
print(len(series))