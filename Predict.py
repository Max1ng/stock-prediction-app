import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTk
import matplotlib.figure as mpl_fig
from matplotlib.backends.backend_agg import FigureCanvasAgg
import PIL
from PIL import Image, ImageTk
import tkinter as tk

class Predict:

    #some cool variables
    def __init__(self) -> None:
        #stock ticker
        self.ticker = None

        self.graph_canvas = None

        self.x = None
        self.y = None
        self.model = None

        #variable to determine how many years of data used in training model
        self.yearsBack = 5

    def setTicker(self, ticker):
        self.ticker = ticker

    def setYearsBack(self, yearsBack):
        self.yearsBack = yearsBack

    #create the dataframes we'll need l8r
    def createDF(self):

        #set todays date and yearsBack years from today
        todaysDate = datetime.date.today()
        todaysDateLastYr = todaysDate - datetime.timedelta(days=365*self.yearsBack)

        #download data using yahoo finance
        stockData = yf.download(self.ticker, start=todaysDateLastYr, end=todaysDate)
        data = pd.DataFrame(stockData['Close'])
        #create a new column "Target" by shifting the "Close" values up 1 (todays closing price would be target for yesterday)
        data['Target'] = data['Close'].shift(-1)

        #drop last row after shifting
        data = data[:-1]

        #df x to "Date" and "Close", df y to "Date" and "Target"
        self.x = data.drop('Target', axis=1)
        self.y = data['Target']

    #train that model!
    def trainModel(self):
        self.model = LinearRegression()
        self.model.fit(self.x, self.y)

    #time to predict :)
    def predictNextYear(self, frame):
        #set todays date and one year from today
        todaysDate = datetime.date.today()
        todaysDateNextYr = todaysDate + datetime.timedelta(days=365)

        #make df for next years worth of dates
        dateRange = pd.date_range(start=todaysDate, end=todaysDateNextYr)

        #make df with "Date" and null values for "Close" (we'll fill these in l8r)
        newStockData = pd.DataFrame({'Date': dateRange, 'Close': [None] * len(dateRange)})

        #set the first prediction value to be the closing value of previous day 
        lastHistoricalValue = self.x.iloc[-1]['Close']
        newStockData.at[0, 'Close'] = lastHistoricalValue

        #iterate through each day, predict next days price, and update df
        for i in range(len(dateRange) - 1):
            #create subset for current day
            currentDaysData = newStockData.iloc[i:i+1].copy()

            #fill in missing values with avg of historical closing values
            mean_close = self.x['Close'].mean()
            currentDaysData['Close'].fillna(mean_close, inplace=True)

            #drop "Date" column and predict next day
            currentDaysData = currentDaysData.drop('Date', axis=1)
            nextDayPrediction = self.model.predict(currentDaysData)

            #update df with predicted value
            newStockData.at[i+1, 'Close'] = nextDayPrediction[0]

        #make graph of predicted prices
        fig = plt.figure(figsize=(6, 4), dpi=100)

        # Add your plot to the Figure
        ax = fig.add_subplot(111)
        ax.plot(newStockData['Date'], newStockData['Close'], label='Predicted Close', color='#41dacb')
        ax.set_xlabel('Date')
        ax.set_ylabel('Stock Price')
        ax.set_title(f'Predicted Stock Prices for {self.ticker}')
        ax.legend()
        ax.set_facecolor("#dbe4eb")

        # Render the Figure to a PNG image
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        width, height = fig.get_size_inches() * fig.get_dpi()
        img = canvas.tostring_rgb()
        photo = PIL.ImageTk.PhotoImage(PIL.Image.frombytes("RGB", (int(width), int(height)), img))

        # If there's an existing image label, remove it
        if hasattr(self, "graph_label"):
            self.graph_label.destroy()

        # Create a Label to display the image
        self.graph_label = tk.Label(frame, image=photo)
        self.graph_label.photo = photo  # Store a reference to avoid garbage collection
        self.graph_label.pack()



        plt.show()

        print(f"Predicted stock prices: {newStockData}")


#run stuff! 
""" if __name__ == "__main__":
    predict = Predict()
    predict.setTicker('AAPL')
    predict.createDF()
    predict.trainModel()
    predict.predictNextYear() """
