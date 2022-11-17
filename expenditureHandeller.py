from datetime import datetime
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class expences:
    def __init__(self):
        self.expencedf = pd.read_csv('expence.csv')

    def newexpence(self):

        date = datetime.today().strftime('%Y-%m-%d')
        title = input("Name of the expence")
        amount = float(input("How much was the expenditure"))

        self.expencedf = self.expencedf.append(pd.DataFrame([
        [date,title,amount]], columns=['date','title','amount']
        
        )).reset_index(drop=True)
        # print(self.salesdf.head())
        self.updateDB()

    def plotlinegraph(self):
        self.expencedf.plot.bar(x='date', y='amount')
        plt.show()

    def datareturn(self):
        return self.expencedf['date'],self.expencedf['amount']

    def updateDB(self):
        self.expencedf.to_csv('expence.csv',index=False)

    def editDB(self):
        index = int(input("what index do you want to edit"))
        amount = int(input("whats the new amount"))
        self.expencedf.at[index,'amount'] = amount
        self.updateDB()

    def outputdf(self):
        print(self.expencedf)


