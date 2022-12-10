import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns 
import os 

PATH = "/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data"
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

# mort = pd.read_csv(os.path.join(PATH, "MORTGAGE30US.csv"), parse_dates=["DATE"], index_col=["DATE"]).loc["2016-09-01":]
# indices = mort.index
# values = mort.values 

final_data = final_data.drop("MORTGAGE30US", axis=1)
print(final_data.info())