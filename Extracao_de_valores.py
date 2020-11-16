from tkinter import *

# Definindo a função

def bt_onclick():
    print(ed.get()) # Retornar o valor contido na entrada da VAR(ed)
    lb["text"] = ed.get() # esta linha irá reescrever o texto coletado na entrada para o Label


#instancia de TK sendo atribuido a variável janela ou qualquer outra var.
janela = Tk()

ed = Entry(janela) #Entry irá criar um campo para digitação do user
ed.place(x=100,y=100)

bt = Button(janela,width =16,text='Submit',command=bt_onclick)
bt.place(x=100,y=130)

lb = Label(janela, text="Resultado")
lb.place(x=130,y=180)

janela.geometry("300x300+200+200")
janela.mainloop()
