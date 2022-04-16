from tkinter import *
from random import choice
app = Tk()
app.title('Color Picker')
app.geometry('300x200')

info = Entry(app)
info.pack()

def show():
    '''Split by comma in info input then random choose'''
    Info = (info.get()).split(',')  
    msg = Label(app, text = choice(Info) )
    msg.pack()

b = Button(app, text = 'Choose', command= show)
b.pack()

app.mainloop()