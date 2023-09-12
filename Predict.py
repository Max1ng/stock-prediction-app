import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        fig = plt.plot(newStockData['Date'], newStockData['Close'], label='Predicted Close', color='#41dacb')
        
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.title(f'Predicted Stock Prices for {self.ticker}')
        plt.legend()
        ax = plt.gca()
        ax.set_facecolor("#dbe4eb")
        
        if self.graph_canvas:
            self.graph_canvas.get_tk_widget().destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        self.graph_canvas = canvas  # Store the current graph canvas
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()


        plt.show()

        print(f"Predicted stock prices: {newStockData}")


#run stuff! 
""" if __name__ == "__main__":
    predict = Predict()
    predict.setTicker('AAPL')
    predict.createDF()
    predict.trainModel()
    predict.predictNextYear() """
