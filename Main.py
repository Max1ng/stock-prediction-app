from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib as plt
import mplfinance as mpf
import tkinter as tk
from tkinter import ttk
import datetime
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Functions(object):
    def __init__(self) -> None:
        self.ticker = '^GSPC'
    
    #return current ticker value
    def returnTicker(self):
        return self.ticker

    #update ticker with button 
    def updateTicker(self, updatedTicker):
        self.ticker = updatedTicker
        print(f'ticker updated to: {self.ticker}')
    
    def button_func():
        print('a button was pressed')

    def exercise_button_func():
        print("hello")

    def getStock(parameter):
        print('ticker inputted')
        print(parameter.get())

    #pull data for specified stock and graph
    def historicalGraph(self):
        try:
            ticker = self.returnTicker()
            startdate = datetime.datetime.now() - datetime.timedelta(days = 365)
            enddate = datetime.datetime.now()
            data = yf.download(ticker, start=startdate, end=enddate)
            mpf.plot(data, type="candle", volume=True, show_nontrading=False, mav= 4)
        except:
            print('Invalid ticker!')
            Functions.updateTicker(self, '^GSPC')
        else:
            print('Graphed')
        #plt.show()
        

def main():

    #call Functions class
    functions = Functions()

    #create the window
    window = tk.Tk()
    window.title('YFinance')
    window.geometry('800x500')
    




    label = ttk.Label(master = window, text = 'This is a test', font= '')
    label.pack()
    
    text = tk.Text(master = window)
    text.pack()


    

    tickerEntry = tk.StringVar(value = '^GSPC')
    entry = ttk.Entry(window, textvariable = tickerEntry)
    entry.pack()

    tickerButton = ttk.Button(master = window, text = 'Change Ticker', command = lambda: functions.updateTicker(tickerEntry.get()))
    tickerButton.pack()

    testButton = ttk.Button(master = window, text = 'Graph', command = functions.historicalGraph)
    testButton.pack()

    
    #Open window
    window.mainloop()
    

main()