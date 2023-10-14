import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro_inexistente_en_catalogo_error import LibroInexistenteEnCatalogoError

class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        try:

            isbn = input("Ingrese el isbn del libro que desea retirar del carrito de compras: ")
            self.tienda_libros.retirar_item_de_carrito(isbn)
        except AttributeError:
            print("El isbn ingresado no está dentro del carrito de compras.")

    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el isbn del libro que desea agregar al carrito de compras: ")
            cantidad = int(input("Ingresa la cantidad de libros que deseas agregar a carrito de compras: "))
            bul = False
            for isbl in self.tienda_libros.catalogo:
                if isbl == isbn:
                    bul = True
            if bul == True:
                self.tienda_libros.agregar_libro_a_carrito(self.tienda_libros.catalogo[isbn],cantidad)
            else:
                print(LibroInexistenteEnCatalogoError(isbn))

        except ExistenciasInsuficientesError as eie:
            print(f"Error: ExistenciasInsuficientesError - {eie}")
        except LibroAgotadoError as lae:
            print(f"Error: LibroAgotadoError - {lae}")
        except ValueError:
            print("Error: El valor que ingresaste no es un número entero")

    # Defina el metodo adicionar_un_libro_a_catalogo
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el isbn del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro (Sin puntos de miles): "))
            existencias = int(input("Ingrese la cantidad de existencias del libro: "))
            self.tienda_libros.adicionar_libro_a_catalogo(isbn,titulo,precio,existencias)
            
        except LibroExistenteError as lee:
            print(f"Error: LibroExistenteError - {lee}")
        except ValueError as e:
            print(f"Error: No cumplir con el tipo de dato que debe ingresar - {e}")
        except LibroError:
            print(f"Error: Debe ingresar un número mayor o igual a 0.")
        