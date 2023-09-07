from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import mplfinance as mpf
import tkinter as tk
from tkinter import ttk
import datetime
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Functions(object):
    def __init__(self) -> None:
        self.ticker = '^GSPC'
        self.graph_canvas = None  # To keep track of the graph canvas

    def returnTicker(self):
        return self.ticker

    def updateTicker(self, updatedTicker):
        self.ticker = updatedTicker
        print(f'ticker updated to: {self.ticker}')

    def button_func(self):  # Added 'self' parameter to these methods
        print('a button was pressed')

    def exercise_button_func(self):
        print("hello")

    def getStock(self, parameter):  # Added 'self' parameter
        print('ticker inputted')
        print(parameter.get())

    def createGraph(self, frame):
        try:
            ticker = self.returnTicker()
            startdate = datetime.datetime.now() - datetime.timedelta(days=365)
            enddate = datetime.datetime.now()
            data = yf.download(ticker, start=startdate, end=enddate)
            fig, ax = mpf.plot(data, type="candle", volume=True, show_nontrading=False, mav=4, returnfig=True)

            for widget in frame.winfo_children():
                widget.destroy()

            if self.graph_canvas:
                self.graph_canvas.get_tk_widget().destroy()  # Destroy the previous graph canvas if it exists

            canvas = FigureCanvasTkAgg(fig, master=frame)
            self.graph_canvas = canvas  # Store the current graph canvas
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()
        except Exception as e:
            print('Invalid ticker!')
            self.updateTicker('^GSPC')  # Changed 'Functions.updateTicker(self, '^GSPC')' to 'self.updateTicker('^GSPC')'
        else:
            print('Graphed')

    def destroyWindow(self, window):
        window.destroy()
        exit()

    
    def windowClose(self, window):
        if window.winfo_exists():
            window.destroy()
            exit()

def main():
    # Call Functions class
    functions = Functions()

    # Create the window
    window = tk.Tk()
    
    window.title('YFinance')
    window.geometry('800x800')

    """ def on_closing():
        if functions.graph_canvas:
            functions.graph_canvas.get_tk_widget().destroy()  # Destroy the graph canvas before closing the window
            window.destroy() """



    label = ttk.Label(master=window, text='This is a test', font=('Ink Free',))
    label.pack()

    text = tk.Text(master=window)
    text.pack()

    graph_frame = ttk.Frame(text)
    graph_frame.pack()

    tickerEntry = tk.StringVar(value='^GSPC')
    entry = ttk.Entry(window, textvariable=tickerEntry)
    entry.pack()

    tickerButton = ttk.Button(master=window, text='Change Ticker', command=lambda: functions.updateTicker(tickerEntry.get()))
    tickerButton.pack()

    testButton = ttk.Button(master=window, text='Graph', command=lambda: functions.createGraph(graph_frame))
    testButton.pack()

    close_button = ttk.Button(master=window, text='Close Window', command=lambda: functions.destroyWindow(window))
    close_button.pack()

    # Open window
    window.protocol("WM_DELETE_WINDOW", lambda: functions.windowClose(window))
    window.mainloop()
    

if __name__ == "__main__":
    main()
    

