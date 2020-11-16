from tkinter import *

janela = Tk()

# propriedade side : Vincula uma extremidade a um componente
# propriedade Anchor : Vincula um sentido a um componente
lb1 = Label(janela, text="Label 1", bg="green")
lb2 = Label(janela, text="Label 2", bg="blue")
lb3 = Label(janela, text="Label 3", bg="yellow")
lb4 = Label(janela, text="Label 4", bg="red")

lb1.pack(side=TOP)
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT, anchor=SW)
lb4.pack(side=BOTTOM, anchor=N)

# Alterar o local dos labels - utilizando o Place
# Gerenciador pack , pode dispor elementos pela tela
# Propriedade Side (TOP,LEFT,RIGHT,BOTTOM)
""" 
Propriedade Anchor 
(N(north)
NW(NORTHWEST)
NE(NORTHEAST)
W(west)
SW(SOUTHWEST)
E(East)
SE(SOUTHEAST)
S(South))

"""
# por padrão , a propriedade side é TOP

janela["bg"] = "black"  # Chave bg = Background
janela.geometry("400x300+200+200")
janela.mainloop()
