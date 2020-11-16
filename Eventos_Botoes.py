from functools import partial
from tkinter import *

# Método geral para retorno de valores
def bt_click(botao):
    print(botao["text"])

"""
def button2_click():
    print('botão 2 clicado')
"""
janela = Tk()

bt1 = Button(janela,width=20,text='você clicou no botão 1')
bt1["command"] = partial(bt_click,bt1)
"""Função(partial) para reescrever  uma função (bt_click)
e assim alocar o valor de bt1 ao no print do mesmo.
sendo assim 
bt1 - com a chave de command  = reescreve a função (bt_click e será passado o parâmetro bt1)
"""

bt1.place(x=100,y=100)
bt2 = Button(janela,width=20,text='você clicou no botão 2')
bt2["command"] = partial(bt_click,bt2)
bt2.place(x=100,y=130)

janela.geometry("300x300+200+200")
janela.mainloop()