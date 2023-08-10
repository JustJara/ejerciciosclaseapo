"""
Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 
Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
"""
import math

class Rectangulo:

    def __init__(self,punto1,punto2):
        self.esquina1 = punto1
        self.esquina2 = punto2
    
    def calcular_perimetro(self):
        distancia_horizontal = self.esquina2.coord_x - self.esquina1.coord_x
        distancia_vertical= self.esquina2.coord_y - self.esquina1.coord_y
        perimetro = (distancia_horizontal*2)+(distancia_vertical*2)
        return perimetro
    
    def calcular_area(self):
        distancia_horizontal = self.esquina2.coord_x - self.esquina1.coord_x
        distancia_vertical= self.esquina2.coord_y - self.esquina1.coord_y
        area = distancia_horizontal * distancia_vertical
        return area
    
    def es_cuadrado(self):
        distancia_horizontal = self.esquina2.coord_x - self.esquina1.coord_x
        distancia_vertical= self.esquina2.coord_y - self.esquina1.coord_y
        if distancia_horizontal == distancia_vertical:
            return "El rectángulo es cuadrado"
        else:
            return "El rectángulo no es cuadrado"


class Punto:
    
    def __init__(self,coord_x,coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y



punto1 = Punto(6,2)
punto2 = Punto(12,4)

rectangulo = Rectangulo(punto1,punto2)

print(f"El perimetro del rectángulo es: {rectangulo.calcular_perimetro()}")
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
print(f"{rectangulo.es_cuadrado()}")