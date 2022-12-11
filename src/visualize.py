import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns 
import os 

PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"


#   Function to create the final dataset
def create_final_data(save = None): 
    data = os.listdir(PATH)
    final_data = pd.DataFrame(columns=[name[:-4] for name in data])
    relevant_dates = pd.read_csv(os.path.join(PATH, data[0]))["DATE"]
    final_data.insert(0, column="DATE", value = pd.read_csv(os.path.join(PATH, data[0]))["DATE"])
    final_data.set_index("DATE", inplace=True)

    for col in final_data.columns:
        name = col + ".csv"
        df = pd.read_csv(os.path.join(PATH, name), parse_dates=["DATE"], index_col=["DATE"])
        try: 
            values = df.loc["1987-01-01":"2022-09-01"]
            final_data[col] = values 
        except:
            continue

    final_data = final_data.drop("MORTGAGE30US", axis=1)
    if save: 
        final_data.to_csv(os.path.join(PATH, "final_data.csv"))

def visualize():
    dataset = pd.read_csv(os.path.join(PATH, "final_data.csv"), parse_dates=["DATE"], index_col=["DATE"])
    cols = dataset.columns
    # for col in dataset:
    #     plt.title(str(col))
    #     dataset[col].plot()
    #     plt.grid()
    #     plt.show()
    #     break 
    
    dataset.plot()
    plt.grid()
    plt.show()
create_final_data(save=True)
visualize()