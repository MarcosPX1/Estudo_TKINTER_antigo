from tkinter import *

janela = Tk()  # Janela principal

lb1 = Label(janela, text='Label 1')
lb2 = Label(janela, text='Label 2')
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)

janela.geometry("500x200+600+200")

janela.mainloop()