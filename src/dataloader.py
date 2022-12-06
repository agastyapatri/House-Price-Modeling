"""
    Python class to load the data. 
"""
import pandas as pd 
import numpy as np 
import os  
import torch 
import torch.nn as nn


class Data(torch.utils.data.Dataset):
    """
        ~ PATH is the source directory containing all the data csv files
        ~ Data.tensor is the data in tensor (multidimensional array) form 
        ~ Data.dataframe is the data as a pandas dataframe 
    """
    def __init__(self, PATH)->None:
        self.path = PATH
        self.tensor = None 
        self.dataframe = None 

    def __getitem__(self, idx):
        #   returning the ith element of the dataset
        pass 


    def getdata(self):
        pass 


if __name__ == "__main__":
    PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"

    #   List of relevant data
    files = os.listdir(PATH)
    file = files[0]
    print(file)
