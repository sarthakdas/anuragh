from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class sales:
    def __init__(self):
        self.salesdf = pd.read_csv('sales.csv')
        self.salesdf.set_index("index", inplace=True)

    def newsale(self):

        date = datetime.today().strftime('%Y-%m-%d')
        title = input("Name of the sale")
        amount = float(input("How much was the sale"))

        self.salesdf = self.salesdf.append(pd.DataFrame([
        [date,title,amount]], columns=['date','title','amount']
        
        )).reset_index(drop=True)
        # print(self.salesdf.head())
        self.updateDB()

    def plotlinegraph(self):
        self.salesdf.plot(x='date', y='amount')
        plt.show()

    def updateDB(self):
        self.salesdf.to_csv('sales.csv')

    def editDB(self):
        index = int(input("what index do you want to edit"))
        amount = int(input("whats the new amount"))
        self.salesdf.loc[index,] = 16

    def outputdf(self):
        print(self.salesdf.head())


