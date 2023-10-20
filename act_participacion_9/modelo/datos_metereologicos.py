
class DatosMetereologicos:

    def __init__(self,nombre_archivo:str):
        self.nombre_archivo = nombre_archivo

        self.suma_temperaturas = 0
        self.cant_temperaturas = 0
        self.temperatura_promedio = 0

        self.suma_humedades = 0
        self.cant_humedades = 0
        self.humedad_promedio = 0

        self.suma_presiones = 0
        self.cant_presiones = 0
        self.presion_promedio = 0

        self.suma_velocidades_viento = 0
        self.cant_velocidades_viento = 0
        self.velocidad_viento_promedio = 0

        self.suma_direcciones_viento = 0
        self.cant_direcciones_viento = 0
        self.direccion_viento_promedio = 0
        self.cantidad_cercana_a_promedio= 999

    def procesar_datos(self) -> tuple[float,float,float,float,str]:
        with open(self.nombre_archivo, "r") as archivo:
            for line in archivo:
                if "Temperatura" in line:
                    temperatura_promedio = self.calcular_temperatura_promedio(line)
                if "Humedad" in line:
                    humedad_promedio = self.calcular_humedad_promedio(line)
                if "Presion" in line:
                    presion_promedio = self.calcular_presion_promedio(line)
                if "Viento" in line:
                    velocidad_viento_promedio, direccion_viento_promedio = self.calcular_velocidad_direccion_viento_promedio(line)
            direccion_viento_str= self.convertir_direccion_float_a_str(self.direccion_viento_promedio)
            print("Datos procesados con éxito, se ha retornado la tupla")
        return (temperatura_promedio,humedad_promedio,presion_promedio,velocidad_viento_promedio,direccion_viento_str)



    def calcular_temperatura_promedio(self, linea:str) -> float:
        temperatura = float(linea.split(':')[1].strip())
        self.suma_temperaturas += temperatura
        self.cant_temperaturas += 1
        self.temperatura_promedio= self.suma_temperaturas/self.cant_temperaturas
        return self.temperatura_promedio
    
    def calcular_humedad_promedio(self, linea: str) -> float:
        humedad = float(linea.split(':')[1].strip())
        self.suma_humedades += humedad
        self.cant_humedades += 1
        self.humedad_promedio = self.suma_humedades/self.cant_humedades
        return self.humedad_promedio
    
    def calcular_presion_promedio(self, linea: str) -> float:
        presion = float(linea.split(':')[1].strip())
        self.suma_presiones += presion
        self.cant_presiones += 1
        self.presion_promedio= self.suma_presiones/self.cant_presiones
        return self.presion_promedio
    
    def calcular_velocidad_direccion_viento_promedio(self,linea: str) -> float:
        velocidad_viento = linea.split(':')[1].strip()
        velocidad_viento = float(velocidad_viento.split(',')[0].strip())
        self.suma_velocidades_viento += velocidad_viento
        self.cant_velocidades_viento += 1
        self.velocidad_viento_promedio=self.suma_velocidades_viento/self.cant_velocidades_viento

        direcciones_viento: dict[str:int] = {"N":0,
                                     "NNE":22.5,
                                     "NE":45,
                                     "ENE":67.5,
                                     "E":90,
                                     "ESE":112.5,
                                     "SE":135,
                                     "SSE":157.5,
                                     "S":180,
                                     "SSW":202.5,
                                     "SW":225,
                                     "WSW":247.5,
                                     "W":270,
                                     "WNW":292.5,
                                     "NW":315,
                                     "NNW":337.5
            }
        direccion_viento = linea.split(":")[1].strip()
        direccion_viento = direccion_viento.split(",")[1].strip()

        for claves in direcciones_viento.keys():
            if direccion_viento == claves:
                self.suma_direcciones_viento += direcciones_viento[claves]
                self.cant_direcciones_viento += 1
        self.direccion_viento_promedio = self.suma_direcciones_viento/self.cant_direcciones_viento
        return self.velocidad_viento_promedio, self.direccion_viento_promedio
        
    def convertir_direccion_float_a_str(self,direccion_viento_promedio : float)-> str:
        direcciones_viento: dict[str:int] = {"N":0,
                                     "NNE":22.5,
                                     "NE":45,
                                     "ENE":67.5,
                                     "E":90,
                                     "ESE":112.5,
                                     "SE":135,
                                     "SSE":157.5,
                                     "S":180,
                                     "SSW":202.5,
                                     "SW":225,
                                     "WSW":247.5,
                                     "W":270,
                                     "WNW":292.5,
                                     "NW":315,
                                     "NNW":337.5
            }
        cantidad_cercana_promedio_str = ''

        for claves in direcciones_viento.keys():
            if direccion_viento_promedio < direcciones_viento[claves]:
                cantidad_cercana_promedio_str = claves
                break 

        return cantidad_cercana_promedio_str
