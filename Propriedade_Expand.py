from tkinter import *
"""
Propriedade Expand irá definir que todos os widges tenham o mesmo tamanho

"""
janela = Tk()

lb1 = Label(janela, text='Linha 1 ', bg='white')
lb2 = Label(janela, text='Linha 2', bg='yellow')
lb3 = Label(janela, text='linha 3', bg='blue')
lb4 = Label(janela, text='linha 4', bg='red')

lb1.pack(side=TOP, fill=BOTH, expand=1)  # Ou True
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry('500x200+600+200')
janela.mainloop()
