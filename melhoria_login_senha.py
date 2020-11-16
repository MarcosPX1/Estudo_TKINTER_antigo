
from tkinter import *

janela = Tk()  # Janela principal


def login():
    
    usuario = ed1.get()
    senha = int(ed2.get())
    if usuario == 'Marcos' and senha == 1020:
        lb3["text"] = 'Acesso concedido'
    else:
        lb3["text"] = 'Errrowwwwww,insira usuário e senha corretos'


lb1 = Label(janela, text='Login:  ')
lb2 = Label(janela, text='Senha:  ')
lb3 = Label(janela, text='')


ed1 = Entry(janela, )
ed2 = Entry(janela, )

bt1 = Button(janela, width=15, text='Confirmar', command=login)

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=3, column=1)

ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)

bt1.grid(row=2, column=1)

janela.geometry("200x100+100+100")
janela.mainloop()
