
import tkinter as tk
from view.interfaz import *

if __name__ == "__main__":

    root = tk.Tk()
    interfaz = InterfazGrafica(root)
    interfaz.estacionamiento.cargar_estado()
    root.mainloop()
    interfaz.estacionamiento.guardar_estado()

