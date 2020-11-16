"""O sentido que um componente terá na célula"""

from tkinter import *

janela = Tk()

lb1 = Label(janela, text='ESPAÇO', width='10', height=3, bg='blue')
lbHORIZONTAL = Label(janela, text='horizontal', bg='yellow')
lbVERTICAL = Label(janela, text='Vertical',bg='red')

lb1.grid(row=0, column=0)
lbHORIZONTAL.grid(row=2, column=0, sticky=W)
lbVERTICAL.grid(row=0, column=1,sticky=N)

janela.geometry('200x100+100+100')

janela.mainloop()
