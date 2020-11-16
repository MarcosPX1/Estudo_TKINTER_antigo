from tkinter import *

janela = Tk()

lb = Label(janela, text='Fala galera!!')

lb.place(x=100, y=100)

#Weight x  Height + X + Y
janela.geometry("300x300+200+200")

janela.mainloop()