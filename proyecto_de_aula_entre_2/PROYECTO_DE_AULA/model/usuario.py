from model.parqueadero import Parqueadero
from model.vehiculo import Vehiculo
from model.vehiculo_inexistente_en_parqueadero import VehiculoInexistenteEnParqueadero
class Usuario:
    

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.parqueadero_asociado = None
        
    def inicializar_parqueadero(self,filas:int,columnas:int):
        self.parqueadero_asociado = Parqueadero(filas,columnas)

    def ingresar_vehiculo_parqueadero(self,indice_fila:int,indice_columna:int,vehiculo:Vehiculo):
        posicion = self.verificar_posicion(indice_fila,indice_columna)
        if posicion == 0:
            self.parqueadero_asociado.parqueadero[indice_fila][indice_columna] = vehiculo
            return True
        elif posicion == type[vehiculo]:
            print(f"La posición actual se encuentra ocupada por el vehículo con placa {vehiculo.placa_vehiculo}")
            return False
        
    def retirar_vehiculo_parqueadero(self,placa_vehiculo):
            for i in range(self.parqueadero_asociado.filas):
                for j in range(self.parqueadero_asociado.columnas):
                    if self.parqueadero_asociado.parqueadero[i][j] != 0 and self.parqueadero_asociado.parqueadero[i][j]!= "reservado":
                        vehiculo = self.parqueadero_asociado.parqueadero[i][j]
                        if placa_vehiculo == vehiculo.placa_vehiculo:
                            self.parqueadero_asociado.parqueadero[i][j] = 0
                            break
                        if vehiculo == 0:
                            raise VehiculoInexistenteEnParqueadero(f"El vehículo con placa {placa_vehiculo} no está ocupando ninguna celda")
            
            return vehiculo

    def reservar_vehiculo_parqueadero(self,vehiculo:Vehiculo,indice_fila:int,indice_columna:int):
        if self.verificar_posicion(indice_fila,indice_columna) == 0:
            self.parqueadero_asociado.parqueadero[indice_fila][indice_columna]= "Reservado"
            print(f"Se ha reservado la celda ({indice_fila},{indice_fila}) al vehiculo con placa '{vehiculo.placa_vehiculo}' exitosamente.")
            return True
        if self.verificar_posicion(indice_fila,indice_columna) == type[Vehiculo]:
            vehicle : Vehiculo = self.parqueadero_asociado.parqueadero[indice_fila][indice_columna]
            print(f"Esta celda se encuentra ocupada por el vehículo con placa {vehicle.placa_vehiculo}")
            print("Revise nuevamente las posiciones que se encuentran disponibles")
            return False

    def verificar_posicion(self,indice_fila:int,indice_columna:int):
        estado = self.parqueadero_asociado.parqueadero[indice_fila][indice_columna]
        return estado