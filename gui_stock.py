
from datetime import date
from tkinter import *
import yfinance as yf
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



style.use('Solarize_Light2')

root = Tk()

root.title("Stock viewer")
root.minsize(500,200)
instruction_text = Label(root, text = "Insert desired stock")
instruction_text.pack(pady=20)

fig = Figure(figsize=(12, 7), dpi=100)
ax = fig.add_subplot()
main_canvas = FigureCanvasTkAgg(fig, master=root)

def clicked(*args):
    ax.clear()
    symbol = ent.get()
    data = yf.Ticker(symbol)
    values = []
    stock_days = []
    currentdate = str(date.today())
    current_year = currentdate.split('-')[0]
    previous_year = int(current_year) - 1
    year_before = currentdate.replace(current_year, str(previous_year))
    realdata = data.history(period='1d', start=year_before, end=currentdate)
    currency = str(data.info['currency'])

    for i in range(0, realdata["Close"].size):
        values.append(realdata["Close"].values[i])
        stock_days.append(i)

    ax.title.set_text(symbol + " Stock")
    ax.plot(stock_days, values, c="blue")
    ax.set_xlabel("Days")
    ax.set_ylabel(f'Value ({currency})')
    ax.set_xticks(list(range(0, realdata["Close"].size+1, 10)))
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="black")
    main_canvas.draw()
    main_canvas.get_tk_widget().pack()


trigger_b = Button(root, text="Show", command=clicked, bg = "black", fg = "white")
trigger_b.pack()

ent = Entry(root)
ent.bind("<Return>", clicked)
ent.pack()

root.mainloop()


