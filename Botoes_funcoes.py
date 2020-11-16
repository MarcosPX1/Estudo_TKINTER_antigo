from tkinter import *


def bt_click():
    print("Botão clicado")
    lb["text"] = "O clique funcionou"


window = Tk()
""" 
Button - invocar um botão para a interface gráfica
Command - serve para dar um comando a partir de uma função
na qual foi criada anteriormente, ao clilcar no botão invocado
"""
bt = Button(window, width=20, text='OK', command=bt_click) #Não invocar o método, remover os parenteses
bt.place(x=100, y=100)

lb = Label(window, text="Teste")
lb.place(x=100, y=150)

window.geometry("300x300+200+200")
window.mainloop()


