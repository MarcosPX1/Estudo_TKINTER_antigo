from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1", bg="green")
lb2 = Label(janela, text="Label 2", bg="blue")
lb3 = Label(janela, text="Label 3", bg="yellow")
lb4 = Label(janela, text="Label 4", bg="red")

lb1.pack(side=TOP)
lb2.pack(side=LEFT)
lb3.pack(side=RIGHT)
lb4.pack(side=BOTTOM)

# Alterar o local dos labels - utilizando o Place
# Gerenciador pack , pode dispor elementos pela tela
# Propriedade Side (TOP,LEFT,RIGHT,BOTTOM)

janela["bg"] = "black" # Chave bg = Background
janela.geometry("400x300+200+200")
janela.mainloop()