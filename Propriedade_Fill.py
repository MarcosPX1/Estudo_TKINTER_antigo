"""
Esta propriedade expande o widge na extremidade definida
com propriedade side
"""
from tkinter import *

janela = Tk()

lb1 = Label (janela, text='Horizontal', bg='blue')
lb2 = Label (janela, text='Vertical', bg='black')
lb3 = Label (janela, text='', bg='blue')

lb1.pack(side=TOP,fill=X)
lb2.pack(side=LEFT,fill=Y)
lb3.pack(side=BOTTOM,fill=X)

janela.geometry('300x200+500+500')
janela.mainloop()
