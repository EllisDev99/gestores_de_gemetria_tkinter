# POSICIONAMIENTO Y DISEÑO
# Gestor de geometría GRID

"""
La forma de utilizarlo es invocando el siguiente método, presente en todos
los widgets:
grid(opciones)

Las opciones posibles son:
• column. Columna en la que se va a colocar el widget (por defecto, la 0).
• columnspan. Número de columnas que ocupa el widget (por defecto, una).
• row. Fila en la que se va a colocar el widget (por defecto, la 0).
• rowspan. Número de filas que ocupa el widget (por defecto, una).
• ipadx. Número de píxeles con los que se rellena el widget horizontalmente, dentro de sus bordes.
• ipady. Número de píxeles con los que se rellena el widget verticalmente, dentro de sus bordes.
• padx. Número de píxeles con los que se rellena el widget horizontalmente, fuera de sus límites.
• pady. Número de píxeles con los que se rellena el widget verticalmente, fuera de sus límites.
• sticky. Determina dónde se ubica el widget dentro de la celda (por
defecto, estaría centrado). Como si de los puntos cardinales de una
brújula se tratara, el valor de esta opción permite situarlo en una
esquina (NE, SE, SW o NW) o centrado en cada uno de los lados de la
celda (N, E, S y W).

Cuando se utiliza este gestor de geometría, el ancho de una columna será
el de su celda más ancha. De la misma manera, la altura de una fila será la
correspondiente a la celda más alta. Si desea cambiar este comportamiento,
use los siguientes métodos de la ventana principal (o widget contenedor):

columnconfigure(columna, opción, ...)
rowconfigure(fila, opción, ...)

Con ellos, podrá configurar aspectos del tamaño de una columna o de una
fila concreta empleando diferentes opciones, entre la que se encuentran:

• minsize. Tamaño mínimo de la columna o de la fila indicada, en
píxeles. Si no hubiera nada dentro, esta no aparecería.
• weight. Permite que el tamaño de una columna o de una fila se
adapte al de la ventana principal (o widget contenedor). El valor
proporcionado establece el peso relativo de esta columna o fila
respecto de las demás a la hora de distribuir el espacio existente.
"""

from tkinter import Tk, Label, TOP, BOTTOM, LEFT, RIGHT

filas = 3
columnas = 4

root = Tk()

for fila in range(filas):
    root.rowconfigure(fila, weight=1) # las filas se adaptan al tamaño de la ventana
    for columna in range(columnas):
        etiqueta = Label(text="Etiqueta"+str(fila)+str(columna), bg='yellow')
        etiqueta.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
        # con sticky="nsew" le decimos que las celdas ocupen todo el tamaño
        root.columnconfigure(columna, weight=1) # las columnas se adaptan al tamaño de la ventana

root.mainloop()