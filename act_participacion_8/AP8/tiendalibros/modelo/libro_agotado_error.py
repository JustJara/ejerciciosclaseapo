from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    

    # Defina metodo inicializador
    def __init__(self, libro: Libro):
        super().__init__(libro)

    # Defina metodo especial

    def __str__(self) -> str:
        return (f"El libro con titulo {self.libro.titulo} e isbn: {self.libro.isbn} ya está agotado")