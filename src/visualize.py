import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns 
import os 

PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"
data = os.listdir(PATH)

final_data = pd.DataFrame(columns=[name[:-4] for name in data])
relevant_dates = pd.read_csv(os.path.join(PATH, data[0]))["DATE"]
final_data.insert(0, column="DATE", value = relevant_dates)
dataframes = [pd.read_csv(os.path.join(PATH, d)) for d in data]

for df in dataframes:
    try:
        # write code to pick out the last 430 elements of the dataframe
        values = df.iloc[-430:, 1]
        final_data[values.name] = values 
    except:
        pass  

print(final_data["DATE", "HSN1F"])

