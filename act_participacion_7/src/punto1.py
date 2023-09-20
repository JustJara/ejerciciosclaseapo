from dataclasses import dataclass

@dataclass
class Elemento:
    nombre:str = ""

    def __eq__(self,other) -> bool:
        return self.nombre == other.nombre

class Conjunto:
    contador: int = 0
    def __init__(self,nombre_conjunto:str):
        self.lista_objetos:list[Elemento] = []
        self.nombre : str = nombre_conjunto
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self,objeto : Elemento) -> bool:
       for elemento in self.lista_objetos:
           if elemento == objeto:
            return True 
       return False
       
    def agregar_elemento(self,objeto:Elemento):
        if self.contiene(objeto) == False:
            self.lista_objetos.append(objeto)
        

    def __add__(self,other):
        AuB = self.unir(other)       
        return AuB

    def unir(self,other):
        AuB = Conjunto({f"{self.nombre} UNIDO {other.nombre}"})
        for elemento in self.lista_objetos:
            AuB.agregar_elemento(elemento)
        for elemento1 in other.lista_objetos:
            AuB.agregar_elemento(elemento1)
        return AuB
    
    @classmethod
    def intersectar(cls,conjunto,conjunto2):
        AnB = Conjunto({f"{conjunto.nombre} intersectado {conjunto2.nombre}"})
        for element in conjunto.lista_objetos:
            for elemento in conjunto2.lista_objetos:
                if element == elemento:
                    AnB.agregar_elemento(elemento)
        return AnB
    
    def __str__(self):
        elementos_str = ', '.join(elem.nombre for elem in self.lista_objetos)
        return f"{self.nombre}: ({elementos_str})"

