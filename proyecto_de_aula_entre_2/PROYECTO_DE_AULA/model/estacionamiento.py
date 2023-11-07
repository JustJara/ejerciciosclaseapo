from model.formato_invalido_error import FormatoInvalidoError
from model.usuario import Usuario
from model.parqueadero import Parqueadero
from model.usuario_existente_error import UsuarioExistenteError
from model.usuario_error import UsuarioError
from model.vehiculo import Vehiculo

from datetime import datetime
import json
import os

class Estacionamiento:
    def __init__(self):
        self.lista_usuario: list[Usuario] = []
        self.lista_vehiculos_en_parqueadero: list[Vehiculo]= []
        self.usuario_actual: Usuario = None
        self.lista_vehiculos_con_reserva : list[Vehiculo] = []
        

    def registrar_usuario(self, nombre_usuario:str, contraseña:str,filas:int,columnas:int):
        usuario = Usuario(nombre_usuario, contraseña)
        for u in self.lista_usuario:
            if usuario.nombre_usuario == u.nombre_usuario:
                raise UsuarioExistenteError(usuario)
        usuario.inicializar_parqueadero(filas,columnas)
        self.lista_usuario.append(usuario)
        return usuario

    def iniciar_sesion_usuario(self, nombre_usuario, contraseña):
        for usuario in self.lista_usuario:
            if nombre_usuario == usuario.nombre_usuario and contraseña == usuario.contraseña:
                print(f"Inicio de sesión exitoso para usuario: {nombre_usuario}")
                self.usuario_actual = usuario
                return True

        print("Usuarios cargados:")
        for usuario in self.lista_usuario:
            print(f"Nombre de usuario: {usuario.nombre_usuario}")

        raise Exception("Nombre de usuario o contraseña incorrectos")

    def cerrar_sesion(self):
        print("Sesión cerrada exitosamente")
        self.usuario_actual = None
                        
    def mostrar_parqueadero(self):
        self.parqueadero.mostrar_parqueadero()

    def ingresar_vehiculo_parqueadero(self,placa_vehiculo:str,hora_ingreso:str,indice_fila:int,indice_columna:int):
        if ':' not in hora_ingreso:
            raise FormatoInvalidoError("Error: La hora de ingreso no cumple con el formato solicitado.")
        else:
            vehiculo = Vehiculo(placa_vehiculo,indice_fila,indice_columna)
            vehiculo.hora_ingreso = hora_ingreso
            for vehiculos in self.lista_vehiculos_con_reserva:
                if vehiculos.placa_vehiculo == placa_vehiculo:
                    self.usuario_actual.ingresar_vehiculo_parqueadero(indice_fila,indice_columna,vehiculo)
                    return "reservado"
            if self.usuario_actual.ingresar_vehiculo_parqueadero(indice_fila,indice_columna,vehiculo):
                self.lista_vehiculos_en_parqueadero.append(vehiculo)
                return True

    def calcular_valor_a_pagar(self,vehiculo:Vehiculo,hora_salida:str):
        costo_x_hora = 3500
        hora_ingreso = vehiculo.hora_ingreso
        hora_ingreso_en_h = float(hora_ingreso.split(":")[0])
        hora_ingreso_en_m = float(hora_ingreso.split(":")[1])
        hora_salida_en_h = float(hora_salida.split(":")[0])
        hora_salida_en_m = float(hora_salida.split(":")[1])
        tiempo_en_horas = abs(hora_salida_en_h - hora_ingreso_en_h) 
        tiempo_en_minutos = abs(hora_salida_en_m - hora_ingreso_en_m)

        if tiempo_en_minutos >= 15:
            cobro_total = tiempo_en_horas * 2 * costo_x_hora
            return cobro_total
        else:
            cobro_total = tiempo_en_horas * costo_x_hora
            return cobro_total
        
    def calcular_valor_pagar_reserva(self,hora_inicio_reserva:str,hora_fin_reserva:str):
        costo_x_hora = 3000
        hora_ingreso_en_h = float(hora_inicio_reserva.split(":")[0])
        hora_ingreso_en_m = float(hora_inicio_reserva.split(":")[1])
        hora_salida_en_h = float(hora_fin_reserva.split(":")[0])
        hora_salida_en_m = float(hora_fin_reserva.split(":")[1])
        tiempo_en_horas = abs(hora_salida_en_h - hora_ingreso_en_h) 
        tiempo_en_minutos = abs(hora_salida_en_m - hora_ingreso_en_m)

        if tiempo_en_minutos >= 1:
            cobro_total = (tiempo_en_horas + 1) * costo_x_hora
            return cobro_total
        else:
            cobro_total = tiempo_en_horas * costo_x_hora
            return cobro_total
    def retirar_vehiculo_parqueadero(self,placa_vehiculo,hora_salida:str,decision_factura:str):
        if ':' not in hora_salida:
            raise FormatoInvalidoError("Error: La hora de ingreso no cumple con el formato solicitado.")
        else:
            vehiculo:Vehiculo = self.usuario_actual.retirar_vehiculo_parqueadero(placa_vehiculo)
            return vehiculo
                

    def reservar_vehiculo_parqueadero(self,hora_inicio_reserva:str,hora_fin_reserva:str,placa:str,indice_fila:int,indice_columna:int):
        if ":" in hora_inicio_reserva and ":" in hora_fin_reserva:
            vehiculo = Vehiculo(placa,indice_fila,indice_columna)
            estado_reserva = self.usuario_actual.reservar_vehiculo_parqueadero(vehiculo,indice_fila,indice_columna)
            if estado_reserva == True:
                cobro_total = self.calcular_valor_pagar_reserva(hora_inicio_reserva,hora_fin_reserva)
                self.lista_vehiculos_con_reserva.append(vehiculo)
                return cobro_total
            if estado_reserva == False:
                return False
        else:
            raise FormatoInvalidoError("Error: La hora de ingreso no cumple con el formato solicitado.")
        
    def generar_factura(self,vehiculo:Vehiculo,hora_salida:str,valor_a_cobrar):
        fecha_hoy = datetime.now()
        mensaje = (
            "---------- Parqueaderos P&J ----------\n"
            f"----- {fecha_hoy} -----\n"
            f"Placa del vehículo: {vehiculo.placa_vehiculo}\n"
            f"Hora de ingreso: {vehiculo.hora_ingreso}\n"
            f"Hora de salida: {hora_salida}\n"
            "Cobro por hora: $3500\n"
            f"Cobro total: {valor_a_cobrar}$\n"
            "---------- Parqueaderos P&J ----------"
            )
        return mensaje

    
    def guardar_estado(self, nombre_archivo="estado.json"):
        estado = {
            "lista_usuario": [usuario.__dict__ for usuario in self.lista_usuario],
            "lista_vehiculos_en_parqueadero": [vehiculo.__dict__ for vehiculo in self.lista_vehiculos_en_parqueadero],
            "lista_vehiculos_con_reserv": [vehiculo.__dict__ for vehiculo in self.lista_vehiculos_con_reserva],
        }

        with open(nombre_archivo, "w") as archivo:
            json.dump(estado, archivo, indent=4, default=self.serializar_objetos)

    def serializar_objetos(self, obj):
        if isinstance(obj, Parqueadero):
            return {
                "filas": obj.filas,
                "columnas": obj.columnas,
                "parqueadero": obj.parqueadero
            }
        elif isinstance(obj, Vehiculo):
            return {
                "placa_vehiculo": obj.placa_vehiculo,
                "celda_ocupada": obj.celda_ocupada,
                "hora_ingreso": obj.hora_ingreso
            }

    
    def cargar_estado(self, nombre_archivo="estado.json"):
        ruta_absoluta = os.path.abspath(nombre_archivo)
        with open(ruta_absoluta, "r") as archivo:
            estado = json.load(archivo)

        self.lista_usuario = []

        for usuario_data in estado.get("lista_usuario", []):
            if "parqueadero_asociado" in usuario_data and usuario_data["parqueadero_asociado"] is not None:
                filas = usuario_data["parqueadero_asociado"]["filas"]
                columnas = usuario_data["parqueadero_asociado"]["columnas"]
                parqueadero = Parqueadero(filas, columnas)

                for i in range(filas):
                    for j in range(columnas):
                        cell_data = usuario_data["parqueadero_asociado"]["parqueadero"][i][j]

                        if cell_data == 0:
                            parqueadero.parqueadero[i][j] = 0
                        elif isinstance(cell_data, dict):
                            vehiculo = Vehiculo(
                                placa=cell_data.get("placa_vehiculo", ""),
                                fila=i,
                                columna=j
                            )
                            vehiculo.hora_ingreso = cell_data.get("hora_ingreso", "")
                            parqueadero.parqueadero[i][j] = vehiculo

                usuario = Usuario(usuario_data["nombre_usuario"], usuario_data["contraseña"])
                usuario.parqueadero_asociado = parqueadero
            else:
                usuario = Usuario(usuario_data["nombre_usuario"], usuario_data["contraseña"])

            self.lista_usuario.append(usuario)
