
class Vehiculo:
    
    def __init__(self, placa:str,fila:int,columna:int):
        self.placa_vehiculo:str = placa
        self.celda_ocupada = (fila,columna)
        self.hora_ingreso:str = None
    
    def __str__(self) -> str:
        return (self.placa_vehiculo)
    

    