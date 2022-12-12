"""
    Defining the model that will be trained to generate a trend. 
"""
import torch 
import torch.nn as nn 
import numpy as np 
import pandas as pd

class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first = True)
        self.fc1 = nn.Linear(hidden_dim, int(hidden_dim/2))
        self.activation = nn.ReLU()
        self.fc2 = nn.Linear(int(hidden_dim/2), output_dim)


    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim, requires_grad=True)

        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim, requires_grad=True)

        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))
        out = self.activation(self.fc1(out[:, -1, :]))
        out = self.fc2(out)
        return out 

if __name__ == "__main__":
    net = RNN(input_dim = 7, hidden_dim = 5,  num_layers = 2,  output_dim = 1)
    testdata = torch.randn(1, 1000, dtype=torch.float32)
    print(net)

