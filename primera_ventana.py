from tkinter import Tk, Label

root = Tk() # se crea la instancia de la clase Tk, que representa la ventana principal

root.title("Curso de Tkinter") # agregando titulo

# VENTANA
root.geometry("800x600") # tamaño de la ventana
root.resizable(True, True) # permite que el usuario cambie el tamaño de la ventana ancho y alto
root.minsize(200, 200) # tamaño mínimo
root.maxsize(960, 720) # tamaño máximo


etiqueta = Label(text="\n !Hola Mundo¡ ") # se crea la etiqueta 'widget' con su texto
etiqueta.pack() # esta sentencia sitúa la etiqueta en la ventana

root.mainloop() # loop infinito que inicia el programa