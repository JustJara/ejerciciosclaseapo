from tiendalibros.modelo.item_compra import ItemCompra
from tiendalibros.modelo.libro import Libro

class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.item : list[ItemCompra] = []

    # Defina el metodo agregar_item
    def agregar_item(self,libro:Libro,cantidad_unidades_libro: int) -> ItemCompra:
        objeto = ItemCompra(libro, cantidad_unidades_libro)
        self.item.append(objeto)
        return objeto
    # Defina el metodo calcular_tota
    def calcular_total(self) -> float:
        total = 0
        for x in self.item:
            total += x.calcular_subtotal() 
        return total
    # Defina el metodo quitar_item
    def quitar_item(self, isbn)-> list[ItemCompra]:
        bool = False
        for items in self.item:
            if items.libro.isbn == isbn:
                bool=True

        if bool== True:
            self.item = [item for item in self.item if item.libro.isbn != isbn]
            print(f"El libro con isbn '{isbn}' se ha retirado exitosamente.")

        else:
            print(f"El libro con isbn '{isbn}' no está en el carrito de compras.")

        return self.item
        