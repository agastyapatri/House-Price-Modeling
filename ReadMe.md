# **Modeling Residential Real Estate in the US**
_Modeling the home prices and the factors that affect the S&P Case-Shiller Home Price Index_ 
*****
## **1. Introduction**
Like any other commodity, the price changes of residential real estate can be broken down into two components: **Supply & Demand.** This project focuses curating a set of features that comprise macro scale supply and demand factors in the US.  

The **Standard and Poors Case Shiller House Prices Index (CSI)** is used as a proxy for house prices. To that end, below is a brief explanation of what CSI tracks.

The CSI is an index which tracks the sale price of single family homes in successive transactions. 
CSI ignores the following:

1. Non Arms Length Transactions.
2. Homes Sold more than once in a 6-month period. 
3. Condominiums and Co-Op property sales. 
4. Newly constructed property.

  
## **2. Supply and Demand Features**
_This section curates a set of factors that affect supply and demand of house prices, which would reflect in the changes in the Case-Shiller Index. It also lists the economic index chosen which tracks this feature._

**2.1   Factors Chosen Which Affect Supply**

1.  New Builds (`HOUST`)
2.  Monthly Supply of New Houses (`MSACSR`)
4.  Number of Sales (`HSN1F`)


**2.2   Factors Chosen Which Affect Demand**

1.  Real Disposable Personal Income: Per Capita (`A229RX0`)
2. Working Age Population (Age 15 - 64) (`LFWA64TTUSM647S`)
3. Population (`POPTHM`) 
4. Unemployment Rate (`UNRATE`)

## **3. Modeling**
The above features were sampled monthly from 1st January 1987 to 1st September 2022. They were combined into a single dataset, with the Case Shiller Index as the target variable. 
The final Dataset has 429 samples, each with 7 features `(429 x 7)`. 

For the purpose of building a Model which is trained on the data, I created LSTM network with the following architecture:

``RNN(``

``  (lstm): LSTM(7, 24, num_layers=20, batch_first=True)``

`` (fc1): Linear(in_features=24, out_features=12, bias=True)``

``  (activation): ReLU()``

`` (fc2): Linear(in_features=12, out_features=1, bias=True)``

``)``

* This network was fed the monthly data, with historical context length of 2 years. This was done to capture macro level economic activity which might affect the Case Shiller Index.

* For training, the Adam Optimizer was used with a **learning rate initiated at 0.0001** and the training was done over **50 epochs**.

* The network was trained on the 429 samples, and achieved a **Mean Squared Error of 3.12942**.

To experiment with different hyperparameters, it is easy to edit all of them in `main.py`


## **3. Results**
_This section breaks down the relationship of each of the above 7 factors and the CSI._
1. **The Per Capita Real Disposable Personal Income (RDPI)** is positively correlated with Home Prices. This is a measure of how much more people can spend on housing, and the more they can spend to service a mortgage, the higher the house price will be pushed. 
2. **The Working age population (Age 15-64)** is positively correlated with home prices. A large working age population implies a larger population with steady employment and incomes. This would result in a larger demand for housing.
3. **Population** is also positively correlated with demand.
4. **Unemployment Rate** is negatively correlated with home prices. This negative correlation appears to be nonlinear, however. 

5. **New Builds:** A higher amount of new construction is negatively correlated to home prices, as it is indicative of a higher rate of supply.
6. **Number of Sales:** A large number of sales is indicative of how many units are leaving the market. A higher number of sales is positively correlated with Home prices. 

For detailed plots of the distributions, please check `figures-results/images/`.

## **Directory Structure**

* `src` contains the source code used to obtain my results.

* `figures-results` contains the results obtained, as well as complimentary figures.

* `data` contains the data used for this analysis

* `main.py` is the driver code that runs performs all the steps of modeling. visualization of the data is done in `src/visualize.py`

