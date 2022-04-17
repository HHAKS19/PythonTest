from tkinter import *

app = Tk()
app.geometry('300x200')

chkbox = StringVar() #IntVar
chk = Checkbutton(app, text='Check', variable= chkbox, onvalue='Yes', offvalue= 'No')
'''for strings, origin checked so deselect(),No need for intvar'''
chk.deselect() #for strings,not for intvar,
chk.pack()

def show():
    msg = Label(app, text = chkbox.get() )
    msg.pack()

b = Button(app, text= 'Show', command= show)
b.pack()
app.mainloop()