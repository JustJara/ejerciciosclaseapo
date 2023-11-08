class ValidadorError(Exception):
    def __init__(self, mensaje:str):
        self.mensaje : str = mensaje


class NoCumpleLongitudMinimaError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class NoTieneLetraMayusculaError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class NoTieneLetraMinusculaError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class NoTieneNumeroError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class NoTieneCaracterEspecialError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


class NoTienePalabraSecretaError(ValidadorError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)