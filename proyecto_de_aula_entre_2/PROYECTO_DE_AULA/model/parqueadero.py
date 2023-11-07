from model.vehiculo import Vehiculo

class Parqueadero:
    VACIO = 0

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.parqueadero: list[list[Vehiculo]] = [[self.VACIO for _ in range(columnas)] for _ in range(filas)]

    def mostrar_parqueadero(self):
        print("------------------------------")
        for fila in self.parqueadero:
            for plaza in fila:
                print(plaza, end="\t")
            print("\n")
        print("------------------------------")



