from tkinter import *

# instanciando Tk, para criação de janelas no código
janela = Tk()


def bt_click(): # Função do click
    print("Soma realizada")
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric(): # Verificando se os valores indicados são de valores numéricos
        num1 = int(ed1.get())
        num2 = int(ed2.get())

        lb2["text"] = num1 + num2
    else:
        lb2["text"] = "Valores informados inválidos"



ed1 = Entry(janela)
ed1.place(x=100, y=100)

ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, text="SOMA", width=16, command=bt_click)
bt.place(x=100, y=150)

lb2 = Label(janela)
lb2.place(x=160, y=200)

lb = Label(janela, text="Resultado: ")
lb.place(x=100, y=200)

janela.geometry("400x300+200+200")
janela.mainloop()
