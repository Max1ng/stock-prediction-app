#imports
from Predict import Predict
from GUI import GUI
import tkinter as tk
from tkinter import ttk

def graphFunctions(frame1, frame2):
    predict.predictNextYear(frame2)
    GUI.createGraph(frame1)


if __name__ == "__main__":
    predict = Predict()
    predict.setTicker('AAPL')
    predict.createDF()
    predict.trainModel()
    #predict.predictNextYear()

    window = tk.Tk()
    
    window.title('YFinance')
    window.geometry('800x800')

    graphFrame1 = ttk.Frame(window)
    graphFrame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Top left corner
    graphFrame2 = ttk.Frame(window)
    graphFrame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # Top right corner

    buttonFrame = ttk.Frame(window)
    buttonFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Centered at the bottom

    tickerEntry = tk.StringVar(value='^GSPC')
    entry = ttk.Entry(buttonFrame, textvariable=tickerEntry)
    entry.grid(row=0, column=0, padx=5, pady=5)

    tickerButton = ttk.Button(buttonFrame, text='Change Ticker', command=lambda: GUI.updateTicker(tickerEntry.get()))
    tickerButton.grid(row=0, column=1, padx=5, pady=5)

    testButton = ttk.Button(buttonFrame, text='Graph', command=lambda: graphFunctions(graphFrame1, graphFrame2))
    testButton.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    close_button = ttk.Button(buttonFrame, text='Close Window', command=lambda: GUI.destroyWindow(window))
    close_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    window.protocol("WM_DELETE_WINDOW", lambda: GUI.windowClose(window))
    window.mainloop()
