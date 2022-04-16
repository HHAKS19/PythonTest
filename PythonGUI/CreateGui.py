from tkinter import *
app = Tk()
'''Widgets'''
app.title('App')
app.geometry('200x200')
display = Label(app, text = 'App window')
'''pack()= top default'''
display.pack(side= RIGHT)
'''main window'''
app.mainloop()  