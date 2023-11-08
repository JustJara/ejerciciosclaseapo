# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod 
from modelo.errores import *

class ReglaValidacion(ABC):
    
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada
    
    def _validar_longitud(self,clave:str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            raise NoCumpleLongitudMinimaError(f"La clave '{clave}' no cumple con la longitud esperada = {self._longitud_esperada} ")

    def _contiene_mayusculas(self,clave:str)->bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        raise NoTieneLetraMayusculaError(f"La clave '{clave}' no tiene letras mayúsculas")

    def _contiene_minusculas(self,clave:str)->bool:
        for caracter in clave:
            if caracter.islower():
                return True
        raise NoTieneLetraMinusculaError(f"La clave '{clave}' no tiene letras minúsculas")

    def _contiene_numero(self,clave:str)-> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        raise NoTieneNumeroError(f"La clave '{clave} no tiene ningún número en ella'")
    
    @abstractmethod
    def es_valida(clave:str)->bool:
        pass

class Validador:

    def __init__(self,regla:ReglaValidacion):
        self.regla = regla

    def es_valida(self,clave:str)->bool:
        return self.regla.es_valida(clave)

class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self,clave:str)->bool:
        for caracter in clave:
            if "@" == caracter:
                return True
            if "_" == caracter:
                return True
            if "#" == caracter:
                return True
            if "$" == caracter:
                return True
            if "%" == caracter:
                return True
        raise NoTieneCaracterEspecialError(f"La clave '{clave}' no tiene ningún caracter especial: @_#$%")
        

    def es_valida(self,clave: str) -> bool:
        longitud = self._validar_longitud(clave)
        mayusculas = self._contiene_mayusculas(clave)
        minusculas=self._contiene_minusculas(clave)
        numero=self._contiene_numero(clave)
        caracter_especial=self.contiene_caracter_especial(clave)
        if longitud == True and mayusculas == True and minusculas == True and numero == True and caracter_especial==True:
            return True
        else:
            raise ValidadorError(f"La clave '{clave} no cumple la Validación Ganímedes'")
    
class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_calisto(self,clave:str)->bool:
        clave_minuscula = clave.lower()
        posicion_calisto = clave_minuscula.find("calisto")
        contador_mayusculas = 0
        posicion_final_calisto = posicion_calisto + 7

        for i in range(posicion_calisto,posicion_final_calisto,1):
            if clave[i].isupper():
                contador_mayusculas += 1
        if contador_mayusculas >= 2 and contador_mayusculas < 7:
            return True
        else:
            raise NoTienePalabraSecretaError(f"La clave '{clave}' no contiene la palabra secreta")

    def es_valida(self,clave:str)->bool:
        longitud = self._validar_longitud(clave)
        numero = self._contiene_numero(clave)
        palabra_secreta = self.contiene_calisto(clave)
        if longitud == True and numero == True and palabra_secreta == True:
            return True
        else:
            raise ValidadorError(f"La clave '{clave}' no cumple la Validación Calisto")