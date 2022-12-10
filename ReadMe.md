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
2.  Monthly Supply of New Houses (MSACSR)
3.  Supply Chain (`Global Supply Chain Pressure Index`)
4.  Number of Sales (`HSN1F`)


**2.2   Factors Chosen Which Affect Demand**

1.  Real Disposable Personal Income: Per Capita (`A229RX0`)
2. Working Age Population (Age 15 - 64) (`LFWA64TTUSM647S`)
3. Population (`POPTHM`)
   
**Note: the feature below needs to be fixed.**
4. 30 year Fixed Rate Mortgage Average (`MORTGAGE30US`)

The expectation is that these 9 features / indices would be able to model the behaviour of the Case Shiller index, and by proxy, model a subsection of real estate price movements. 

## **3. Results**
_What have the methods achieved?_

### **3.1 Univariate Analyses**
_This subsection breaks down the relationship of each of the above 9 factors and the CSI._

### **3.2 Multivariate Analysis**

## **Directory Structure**

* `src` contains the source code used to obtain my results.

* `figures-results` contains the results obtained, as well as complimentary figures.

* `data` contains the data used for this analysis

* final results are in `report.pdf`