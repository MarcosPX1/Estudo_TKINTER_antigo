import tkinter as tk


window = tk.Tk()
window.title("Janela Principal") # Altera o título da janela
window["bg"] = "green" # Duas formar de definir o parâmetro background
window["background"] = "red"

# Largura x Altura + distância da margem  esquerda  +  distancia do topo
# 300x300+100+100
window.geometry("800x600+500+100")

window.mainloop() # Looping infinito para que seja realizado algo na janela

