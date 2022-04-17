from tkinter import *
from random import choice

app = Tk()
app.title('Color Picker')
app.geometry('450x100')
app['background'] = '#2a363b'
# hex code color, capital letters also acceptable

info = Entry(app, background= 'grey', foreground= 'black')

'''For entry input, from row 0 to 2 columns'''
'''Padding for pixel position far away from margin '''
info.grid(row = 0, column= 0, columnspan= 2, padx= 20, pady= 5)

def show():

    '''Split by comma in info input then random choose'''
    Info = (info.get()).split(',')  
    Choice = 'Choice: ' + str(choice(Info))
    msg = Label(app, text = Choice, font= ('Courier',12), background= 'black', foreground= 'silver')
    
    '''column 0 so random numbers keep replacing at col 0'''
    msg.grid(row= 0, column= 2, padx= 20, pady= 5)

    if quitb['state'] == DISABLED:
        quitb['state'] = NORMAL 

b = Button(app, text = 'Choose', command= show, background= 'white', foreground= 'cyan')
b.grid(row= 1, column= 0, padx= 20, pady= 5)

quitb = Button(app, text = 'Cancel', command= app.quit, state = DISABLED, background= 'black', foreground= 'orange')
quitb.grid(row= 1, column= 1, padx= 20, pady= 5)
app.mainloop()