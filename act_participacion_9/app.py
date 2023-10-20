
from modelo.datos_metereologicos import DatosMetereologicos



dm = DatosMetereologicos("act_participacion_9/datos.txt")
print(dm.procesar_datos())
