import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df = pd.read_csv("CSUSHPISA.csv")

x = df.iloc[:, 0]
y = df.iloc[:, 1]

plt.plot(x,y)
plt.grid()
plt.show()
