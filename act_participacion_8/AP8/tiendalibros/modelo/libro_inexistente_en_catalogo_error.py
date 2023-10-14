class LibroInexistenteEnCatalogoError(Exception):
    
    def __init__(self, isbn:str):
        self.isbn : str  = isbn

    def __str__(self) -> str:
        return (f"El libro con isbn: '{self.isbn}' no existe en el catálogo")