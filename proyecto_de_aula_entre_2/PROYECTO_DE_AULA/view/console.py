from model.estacionamiento import Estacionamiento
from model.usuario_existente_error import UsuarioExistenteError
from model.usuario_error import UsuarioError
from model.vehiculo_inexistente_en_parqueadero import VehiculoInexistenteEnParqueadero

class UIConsola:

    def __init__(self):
        self.estacionamiento: Estacionamiento = Estacionamiento()

    
    def registrar_usuario(self):
        try:
            print("------------------------")
            print("Bienvenido al sistema de parqueaderos P&J")
            print("Para registrarte debes seguir las instrucciones")
            print("Ingresa el nombre de usuario: ")
            nombre_usuario: str = str(input())
            print("Ingrese la contraseña: ")
            contraseña: str = str(input())
            print("Ingrese el tamaño del parqueadero")
            filas = int(input("Ingrese la cantidad de filas del parqueadero: "))
            columnas = int(input("Ingrese la cantidad de columnas del parqueadero: "))
            usuario = self.estacionamiento.registrar_usuario(nombre_usuario, contraseña, filas,columnas)
            print(f"Usuario {usuario.nombre_usuario} registrado exitosamente")
            print(f"Parqueadero de {usuario.nombre_usuario} creado y asociado exitosamente")
            
        except UsuarioExistenteError as uee:
            print(f"Error: UsuarioExistenteError - {uee}")


    def crear_parqueadero(self):
        print("------------------------")
        print("Para crear el parqueadero asociado sigue las instrucciones")
        print("Ingresa la cantidad de filas del parqueadero: ")
        filas = int(input())
        print("Ingresa la cantidad de columnas")
        columnas = int(input())
        parqueadero = self.estacionamiento.inicializar_parqueadero(filas,columnas)
        return parqueadero
    
    def iniciar_sesion(self):
        print("------------------------")
        print("Para iniciar sesión debes de seguir las instrucciones.")
        print("Ingresa el nombre de usuario")
        nombre_usuario = str(input())
        print("Ingrese la contraseña")
        contraseña = str(input())
        try:
                if self.estacionamiento.iniciar_sesion_usuario(nombre_usuario, contraseña):
                    return True
        except UsuarioError as ue:
            print(f"Error: {ue}")
            return False


    def ejecutar_app(self):
        while True:
            self.mostrar_menu_inicial()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.registrar_usuario()
            if opcion == 2:
                if self.iniciar_sesion():
                    self.ejecutar_app_dentro()
            if opcion == 3:
                print("¡Vuelve pronto!")
                break
        
    def ejecutar_app_dentro(self):
        while True:
            self.mostrar_menu_dentro_app()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.mostrar_parqueadero()
            if opcion == 2:
                self.ingresar_vehiculo()
            if opcion == 3:
                self.retirar_vehiculo()
            if opcion == 4:
                self.reservar_celda_parqueadero()
            if opcion == 5:
                print("Sesión cerrada exitosamente")
                break

    @staticmethod
    def mostrar_menu_inicial():
        print("------------------------")
        print("Escoje la opción según lo que deseas hacer")
        print("1. Registrarse")
        print("2. Logearse")
        print("3. Salir")
        print("------------------------")

    @staticmethod
    def mostrar_menu_dentro_app():
        print("------------------------")
        print("Escoge la opción según lo que quieras hacer")
        print("1. Mostrar parqueadero")
        print("2. Ingresar vehiculo")
        print("3. Retirar vehiculo")
        print("4. Reservar celda para un vehículo")
        print("5. Cerrar sesión")
        print("------------------------")

    def mostrar_parqueadero(self):
        usuario_actual = self.estacionamiento.usuario_actual  
        if usuario_actual:
            usuario_actual.parqueadero_asociado.mostrar_parqueadero()
        else:
            print("Ningún usuario logueado.")

    def ingresar_vehiculo(self):
        usuario_actual = self.estacionamiento.usuario_actual 
        if usuario_actual:
            print("-------------------------")
            placa_vehiculo = str(input("Ingrese la placa del vehículo: "))
            print("Inrese la hora en la que ingresó el vehículo con el siguiente formato 00:00")
            hora_ingreso = str(input("Ingreselo aquí: "))
            indice_fila = int(input("Ingrese el índice de la fila: "))
            indice_columna = int(input("Ingrese el índice de la columna: "))
            if self.estacionamiento.ingresar_vehiculo_parqueadero(placa_vehiculo,hora_ingreso,indice_fila,indice_columna):
                print("El vehículo se ingresó con éxito")

    def retirar_vehiculo(self):
        try:
            usuario_actual = self.estacionamiento.usuario_actual
            if usuario_actual:
                print("-------------------------")
                placa_vehiculo = str(input("Ingrese la placa del vehiculo: "))
                print("Inrese la hora en la que retiró el vehículo con el siguiente formato 00:00 y en 24h")
                hora_salida = str(input("Ingrese la hora de salida: "))
                decision_factura = str(input("¿Desea generar factura? ('si' , 'no')"))
                self.estacionamiento.retirar_vehiculo_parqueadero(placa_vehiculo,hora_salida,decision_factura)
        except VehiculoInexistenteEnParqueadero as viep:
            print(viep.mensaje)

    def reservar_celda_parqueadero(self):
        usuario_actual = self.estacionamiento.usuario_actual
        if usuario_actual:
            print("-------------------------")
            self.mostrar_parqueadero()
            print("Ingrese las horas para reservar la celda con el siguiente formato 00:00 y en 24h.")
            hora_inicio_reserva = str(input("Ingrese la hora de inicio aquí: "))
            hora_fin_reserva = str(input("Ingrese la hora hasta quiere tener reservado: "))
            placa = str(input("Ingrese la placa del vehículo: "))
            indice_fila = int(input("Ingrese la posición de la fila a reservar: "))
            indice_columna = int(input("Ingrese la posición de la columna a reservar: "))
            self.estacionamiento.reservar_vehiculo_parqueadero(hora_inicio_reserva,hora_fin_reserva,placa,indice_fila,indice_columna)

