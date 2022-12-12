"""
    Training the model
"""
import numpy as np 
import torch 
import torch.nn as nn 
from model import RNN
from dataset import Data
import time 
import os 

class Trainer(nn.Module):
    def __init__(self, model, dataloader, num_epochs, lr):
        super().__init__()
        self.dataloader = dataloader
        self.num_epochs = num_epochs
        self.network = model 
        self.optimizer = torch.optim.Adam(model.parameters(), lr = lr)
        self.loss_fun = nn.MSELoss()
        
    def train_one_epoch(self, epoch):
        #   Function to iterate over the dataset
        self.network.train(True)
        running_loss = 0.0
        length = len(self.dataloader)
        

        for i, data in enumerate(self.dataloader):
            sample, target = data 
            sample = sample.unsqueeze(0)
            target = target.unsqueeze(0)

            output = self.network(sample)
            loss = self.loss_fun(output, target)
            
            #   backpropagation 
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            running_loss += loss.item()
            
            # reporting after one epoch of training
            if (i+1)%length == 0:
                avg_epoch_loss = running_loss / length 
                print(f"Training Epoch: {epoch+1} | Epoch Loss = {round(avg_epoch_loss, 5)}")

        return self.network, avg_epoch_loss
    
    def train_all_epochs(self, save=None, root=None):
        #   Function to iterate over all the epochs
        training_loss = []

        start = time.time()
        for e in range(self.num_epochs):
            trained_network, epoch_loss = self.train_one_epoch(epoch=e)
            training_loss.append(epoch_loss)
        end = time.time()
        print(f"Training Done. Time Taken to Train = {round((end - start)/60, 3)} mins")
        print(f"Mean Squared Error at the end {self.num_epochs} epochs is: {round(training_loss[-1], 5)}")

        if save:
            torch.save(trained_network.state_dict(), root)
        return trained_network


if __name__ == "__main__":
 
    dataset = Data(path="/home/agastyapatri/Projects/MachineLearning/House-Price-Modeling/data/final_data.csv")       
 
    dataloader = torch.utils.data.DataLoader(dataset, batch_size = 1, shuffle=False)
 
    network = RNN(input_dim = 7, hidden_dim = 25,  num_layers = 18,  output_dim = 1)

    trainer = Trainer(model = network, dataloader=dataloader, num_epochs=50, lr=0.0001)

    # print(trainer.train_all_epochs())