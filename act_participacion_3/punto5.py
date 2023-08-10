
""""
Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
 """

import math

class Circulo:

    def __init__(self,centro,radio):
        self.centro = centro
        self.radio = radio
        print(centro)
        print(radio)

    def calcular_area(self):
        return math.pi * (self.radio**2)
    
    def calcular_perimetro(self):
        d = self.radio*2
        perimetro = d * (math.pi)
        return perimetro
    
    def punto_pertenece_circulo(self,punto):
        distancia_entre_punto_centro = math.sqrt((punto.coord_x - self.centro.coord_x)**2 + (punto.coord_y - self.centro.coord_y)**2)
        if distancia_entre_punto_centro <= self.radio :
            print(f"El punto pertenece al circulo")
        else:
            print(f"El punto no pertenece al circulo")

class Punto:
    
    def __init__(self,coord_x,coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

centro = Punto(0,0)
radio = 2

circulo = Circulo(centro,radio)
punto1 = Punto(4,6)
punto2 = Punto(1,1)
print(f"El área del circulo es: {circulo.calcular_area()}")
print(f"El perimetro del circulo es: {circulo.calcular_perimetro()}")
circulo.punto_pertenece_circulo(punto1)
circulo.punto_pertenece_circulo(punto2)