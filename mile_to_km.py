from tkinter import *


#initialize global variables as window and labels
WINDOW = Tk()
BLANK = Label(text='                   ')
IS_EQUAL = Label(text='is equal to', font=('Arial', 12, 'bold'))
MILES = Label(text='Miles', font=('Arial', 12, 'bold'))
KM = Label(text='Km', font=('Arial', 12, 'bold'))
ANSWER = Label(text='0', font=('Arial', 12, 'bold'))


#window configurations
WINDOW.title('Mile to KM Converter')
WINDOW.minsize(width=400, height=200)
INPUT = Entry(width=12, justify='center')
BLANK.grid(ipadx=35, ipady=30)
IS_EQUAL.grid(column=0, row=1)
INPUT.grid(column=2, row=0)
MILES.grid(column=3, row=0, padx=35)
KM.grid(column=3, row=1, padx=35)
ANSWER.grid(column=2, row=1)


def calculate_clicked():
    '''Miles to kilometers conversion and relevant configurations to display input into window.'''
    new_text = int(INPUT.get())
    new_text *= 1.609344
    ANSWER.config(text=int(new_text))


#global variable located here because python does not support hoisting
CALCULATE = Button(text='Calculate', command=calculate_clicked)
CALCULATE.grid(column=2, row=3, pady=20)


#necessary for tkinter windows
WINDOW.mainloop()