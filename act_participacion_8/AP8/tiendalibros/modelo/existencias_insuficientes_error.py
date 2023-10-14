from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):


    # Defina metodo inicializador
    def __init__(self, libro: Libro, cantidad_a_comprar:int):
        super().__init__(libro)
        self.cantidad_a_comprar : int = cantidad_a_comprar
    # Defina metodo espcial
    def __str__(self) -> str:
        return (f"El libro con titulo '{self.libro.titulo}' e isbn '{self.libro.isbn}' no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}")
