""""
Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto
 (se pasan como parámetros en el constructor).Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
 """

class Carta:

    DIAMANTE = "Diamantes"
    TREBOL = "Trébol"
    PICA = "Pica"
    CORAZON = "Corazón"

    def __init__(self,valor,pinta):
        self.valor = valor
        self.pinta = pinta
