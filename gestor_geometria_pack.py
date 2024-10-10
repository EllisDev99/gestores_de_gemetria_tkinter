# POSICIONAMIENTO Y DISEÑO
# Gestor de geometría PACK
from tkinter import Tk, Label, TOP, BOTTOM, LEFT, RIGHT

root = Tk() # se crea la instancia de la clase Tk, que representa la ventana principal

# VENTANA
root.title("POSICIONAMIENTO Y DISEÑO (PACK)") # agregando titulo
root.geometry("200x200")

# ETIQUETAS
etiqueta1 = Label(text="Etiqueta1")
etiqueta2 = Label(text="Etiqueta2")
etiqueta3 = Label(text="Etiqueta3")
etiqueta4 = Label(text="Etiqueta4")

# asignamos la posición de cada ventana y le colocamos un padding externo de 10px sea en el eje X o Y dependiendo de su posición
etiqueta1.pack(side=TOP, pady=10)
etiqueta2.pack(side=BOTTOM, pady=10)
etiqueta3.pack(side=LEFT, padx=10)
etiqueta4.pack(side=RIGHT, padx=10)

root.mainloop() # loop infinito que inicia el programa