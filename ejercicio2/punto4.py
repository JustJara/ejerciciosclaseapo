"""
Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 
Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
"""
import math

class Rectangulo:

    def __init__(self,punto1,punto2,punto3,punto4):
        self.esquina1 = punto1
        self.esquina2 = punto2
        self.esquina3 = punto3
        self.esquina4 = punto4
    
    def calcular_perimetro(self):
        distancia_horizontal = math.sqrt((self.esquina2.coord_x - self.esquina1.coord_x)**2 + (self.esquina2.coord_y - self.esquina1.coord_y)**2)
        distancia_vertical= math.sqrt((self.esquina3.coord_x - self.esquina1.coord_x)**2 + (self.esquina3.coord_y - self.esquina1.coord_y)**2)
        perimetro = (distancia_horizontal*2)+(distancia_vertical*2)
        return perimetro
    
    def calcular_area(self):
        distancia_horizontal = math.sqrt((self.esquina2.coord_x - self.esquina1.coord_x)**2 + (self.esquina2.coord_y - self.esquina1.coord_y)**2)
        distancia_vertical= math.sqrt((self.esquina3.coord_x - self.esquina1.coord_x)**2 + (self.esquina3.coord_y - self.esquina1.coord_y)**2)
        area = distancia_horizontal * distancia_vertical
        return area
    
    def es_cuadrado(self):
        distancia_horizontal = math.sqrt((self.esquina2.coord_x - self.esquina1.coord_x)**2 + (self.esquina2.coord_y - self.esquina1.coord_y)**2)
        distancia_vertical= math.sqrt((self.esquina3.coord_x - self.esquina1.coord_x)**2 + (self.esquina3.coord_y - self.esquina1.coord_y)**2)
        if distancia_horizontal == distancia_vertical:
            return "El rectángulo es cuadrado"
        else:
            return "El rectángulo no es cuadrado"


class Punto:
    
    def __init__(self,coord_x,coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

punto1 = Punto(1,1)
punto2 = Punto(11,1)
punto3 = Punto(1,4)
punto4 = Punto(11,4)

rectangulo = Rectangulo(punto1,punto2,punto3,punto4)

print(f"El perimetro del rectángulo es: {rectangulo.calcular_perimetro()}")
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
print(f"{rectangulo.es_cuadrado()}")