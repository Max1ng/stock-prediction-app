import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import yfinance as yf
import mplfinance as mpf
class GUI: 
    def __init__(self) -> None:
        self.ticker = '^GSPC'
        self.graph_canvas = None  # To keep track of the graph canvas

    def returnTicker(self):
        return self.ticker

    def updateTicker(self, updatedTicker):
        self.ticker = updatedTicker
        print(f'ticker updated to: {self.ticker}')

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

    