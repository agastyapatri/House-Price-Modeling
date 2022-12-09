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
        """
            1. concatenating the data
        """
        #   List of relevant data
        files = os.listdir(self.path)[1:]
        target = pd.read_csv(os.path.join(self.path, os.listdir(self.path)[0]))
        cols = [file[:-4] for file in files]
        data = []
        features = pd.DataFrame(columns= cols)
        relevant_dates = target["DATE"]

        for col in cols:
            name = col + ".csv"
            try: 
                df = pd.read_csv(os.path.join(self.path, name))[-429:]
                features[col] = df[col]
            
            except:
                continue 

        # print(features)
        print(relevant_dates[-50:])





        


                



if __name__ == "__main__":
    PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"
    data = Data(PATH=PATH)
    data.getdata()
    