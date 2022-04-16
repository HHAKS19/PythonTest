from tkinter import *
from random import choice

app = Tk()
app.title('Color Picker')
app.geometry('450x100')

info = Entry(app)
'''For entry input, from row 0 to 2 columns'''
'''Padding for pixel position far away from margin '''
info.grid(row = 0, column= 0, columnspan= 2, padx= 20, pady= 5)

def show():
    '''Split by comma in info input then random choose'''
    Info = (info.get()).split(',')  
    Choice = 'Choice: ' + str(choice(Info))
    msg = Label(app, text = Choice)
    '''column 0 so random numbers keep replacing at col 0'''
    msg.grid(row= 0, column= 2, padx= 20, pady= 5)

    if quitb['state'] == DISABLED:
        quitb['state'] = NORMAL 

b = Button(app, text = 'Choose', command= show)
b.grid(row= 1, column= 0, padx= 20, pady= 5)

quitb = Button(app, text = 'Cancel', command= app.quit, state = DISABLED)
quitb.grid(row= 1, column= 1, padx= 20, pady= 5)

app.mainloop()