#imports
from Predict import Predict
from GUI import GUI
import tkinter as tk
from tkinter import ttk

def graphFunctions(frame1, frame2):
    GUI.createGraph(frame1)
    predict.predictNextYear(frame2)
   


if __name__ == "__main__":
    predict = Predict()
    predict.setTicker('AAPL')
    predict.createDF()
    predict.trainModel()
    #predict.predictNextYear()
    
    GUI = GUI()

    #create the window
    window = tk.Tk()
    
    window.title('YFinance')
    window.geometry('1200x800')


    label = ttk.Label(master=window, text='This is a test', font=('Ink Free',))
    label.pack()

    tickerButton = ttk.Button(master=window, text='Change Ticker', command=lambda: GUI.updateTicker(tickerEntry.get()))
    tickerButton.pack(side='bottom')

    testButton = ttk.Button(master=window, text='Graph', command=lambda: graphFunctions(graphFrame, graphFrame2))
    testButton.pack(side='bottom')

    close_button = ttk.Button(master=window, text='Close Window', command=lambda: GUI.destroyWindow(window))
    close_button.pack(side='bottom')

    historicalGraph = tk.Text(master=window)
    historicalGraph.pack(side='left', fill='both', expand=False)

    predictedGraph = tk.Text(master=window)
    predictedGraph.pack(side='right', fill='both', expand=False)
  
    graphFrame = ttk.Frame(historicalGraph, width=600, height=400)
    graphFrame.pack(fill='both', expand=False)

    graphFrame2 = ttk.Frame(predictedGraph, width=600, height=400)
    graphFrame2.pack(fill='both', expand=False)

    tickerEntry = tk.StringVar(value='^GSPC')
    entry = ttk.Entry(window, textvariable=tickerEntry)
    entry.pack()

    

    #close window on close 🙏
    window.protocol("WM_DELETE_WINDOW", lambda: GUI.windowClose(window))
    #open window
    window.mainloop()





#teehee
"""                                                                     ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;` """