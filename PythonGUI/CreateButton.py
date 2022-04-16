from tkinter import *
from random import randint
app = Tk()
app.title('App')
app.geometry('200x200')

def sho_msg():
    msg = Label(app, text = 'Go to hell', fg = 'red')  #text = randint(1,100) 
    msg.pack()
'''command = no parenthesis'''
b = Button(app, text = 'Click', command= sho_msg )
b.pack()
app.mainloop()
