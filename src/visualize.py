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



def visualize(option):
    dataset = pd.read_csv(os.path.join(PATH, "final_data.csv"), parse_dates=["DATE"], index_col=["DATE"])
    dataset = dataset.drop("final_data", axis=1)

    demand_cols = ["UNRATE", "POPTHM", "LFWA64TTUSM647S", "A229RX0"]
    supply_cols = ["HOUST", "MSACSR", "HSN1F"]  
    cols = dataset.columns
    target = dataset["CSUSHPISA"]

    #   Plotting the features: both supply and demand 
 
    if option == "univariate":
        for col in supply_cols: 
            ax1 = plt.subplot(1, 2, 1)
            ax1.scatter(dataset[col].values, target.values, s = 5)
            plt.grid()
            plt.xlabel(f"{col}")
            plt.ylabel("CSUSHPISA")
            ax1.set_title(f"Case Shiller Index vs {col}")

            ax2 = plt.subplot(1,2,2)
            ax2.plot(dataset[col].index, dataset[col].values)
            ax2.set_title(f"{col} vs time")
            plt.xlabel("time (months)")
            plt.grid()

            plt.show()

    if option == "time":
        plt.title(f"Features affecting the Supply of housing")
        for col in supply_cols:
            plt.plot(dataset[col].index, dataset[col].values, label=f"{col} vs time")
        plt.grid()
        plt.legend()
        plt.show()

    if option == "corr":
        pass 

visualize(option = "time")

