import math

class Punto:
    
    def __init__(self,coord_x,coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

#Método mostrar que imprima por consola las coordenadas del punto
    def mostrar_coordenadas(self):
        print(f"({self.coord_x}, {self.coord_y})")
    
    def mover_coordenadas_punto(self,mover_x,mover_y):
        self.coord_x = mover_x
        self.coord_y = mover_y
    def calcular_distancia_entre_puntos(self,punto2):
        distancia = math.sqrt((punto2.coord_x - self.coord_x)**2 + (punto2.coord_y - self.coord_y)**2)
        return distancia

punto1= Punto(2, 1)
punto2= Punto(4,2)
punto1.mostrar_coordenadas()
#punto1.mover_coordenadas_punto(5,2)
punto1.mostrar_coordenadas()
print(punto1.calcular_distancia_entre_puntos(punto2))




