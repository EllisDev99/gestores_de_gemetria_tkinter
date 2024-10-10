from tkinter import Tk, Label

root = Tk() # se crea la instancia de la clase Tk, que representa la ventana principal

root.title("Curso de Tkinter") # agregando titulo

root.geometry("200x200") # tamaño de la ventana

etiqueta = Label(text="\n !Hola Mundo¡ ") # se crea la etiqueta 'widget' con su texto
etiqueta.pack() # esta sentencia sitúa la etiqueta en la ventana

root.mainloop() # loop infinito que inicia el programa