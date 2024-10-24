# POSICIONAMIENTO Y DISEÑO
# Gestor de geometría PLACE
"""
Este gestor, a diferencia de los dos anteriores, permite colocar los widgets en
coordenadas específicas de la ventana principal (o widget contenedor). Para
utilizarlo, se debe llamar al siguiente método, disponible en todos los widgets:

place(opciones)

Las opciones de las que dispone son:
* anchor. Indica cómo situar el widget en la ventana, tomando como referencia las 
coordenadas (x, y) contenidas en las opciones x e y (se describen más abajo). 
Su valor puede ser N, S, E, W, NE, NW (predeterminado, esquina superior izquierda 
del widget), SE, SW o CENTER. La siguiente imagen lo muestra gráficamente (el cuadrado
representa el widget tal como quedaría ubicado respecto del punto de referencia,
dependiendo del valor de esta opción):

* bordermode. Determina si las coordenadas especificadas usan como
referencia el interior del widget contenedor (INSIDE, valor por
defecto) o el exterior (OUTSIDE).

• height, width. Alto y ancho del widget en píxeles.

• relheight, relwidth. Ancho y alto del widget, tomado de forma
relativa al ancho y alto de la ventana principal (o widget contenedor).
Por lo tanto, determina sus dimensiones como una fracción de la
ventana. Su valor estará comprendido entre 0,0 y 1,0; por ejemplo, si el
alto de la ventana principal fuera de 800 píxeles y el valor de la opción
relheight de uno de los widgets fuera de 0,25, su alto sería de 200
píxeles. La utilidad de este método es ajustar el tamaño de los widgets
al de la ventana (o widget contenedor), cuando esta se modifique.

• x. Coordenada x del punto utilizado como referencia para situar el
widget en la ventana principal (o widget contenedor). Su valor viene
dado en píxeles. Las coordenadas (0, 0) corresponden a la esquina
superior izquierda de la ventana principal (o widget contenedor).

• y. Coordenada y del punto utilizado como referencia para situar el
widget en la ventana principal (o widget contenedor).

• relx, rely. Posición relativa, tanto horizontal como vertical, repre-
sentada como una fracción del alto y ancho de la ventana principal (o
widget contenedor). Su valor, de nuevo, estará comprendido entre 0,0
y 1,0; por ejemplo, si el ancho de una ventana fuera de 500 píxeles
y relx tuviera el valor 0,5, la coordenada x del widget sería 250. La
utilidad de esta opción es mantener la posición de los widgets, aunque
cambie el tamaño de la ventana.

Por último, para dejar de mostrar un widget situado previamente en la
ventana principal (o widget contenedor), se debe ejecutar el método:

place_forget()
"""

from tkinter import Tk, Label

root = Tk()
root.geometry("200x200")

etiqueta = Label(text="Etiqueta")
#etiqueta.place(x=100, y=100, anchor="center")
etiqueta.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

"""
El problema viene cuando se cambia el tamaño de la ventana. En ese caso, la
etiqueta se mantendrá fija en las mismas coordenadas (100, 100), y dejará
de estar centrada.

Para resolverlo, puede evitar que el usuario modifique las dimensiones de
la ventana con el método resizable(), o utilizar las opciones relx y rely
(en vez de x e y) en el método place(). De esa forma, la posición de la
etiqueta será relativa al tamaño de la ventana (no absoluta). Así, cuando
la ventana se redimensione, la etiqueta seguirá estando centrada (en la
misma posición relativa).
Por lo tanto, sustituya la sentencia

etiqueta.place(x=100, y=100, anchor="center")

por:

etiqueta.place(relx=0.5, rely=0.5, anchor="center")

Vuelva a ejecutar el programa. Tal como se acaba de comentar, ahora la
etiqueta aparecerá centrada, independientemente de las dimensiones de
la ventana
"""

"""
Se desaconseja el uso de este gestor de geometría (salvo en casos excepcio-
nales), ya que requiere especificar la posición absoluta de cada elemento.
Cualquier cambio posterior supondría rehacer de nuevo toda la interfaz.
"""