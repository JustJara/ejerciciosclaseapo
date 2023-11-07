from model.usuario import Usuario
from model.usuario_error import UsuarioError

class UsuarioExistenteError(UsuarioError):

    def __init__(self, usuario: Usuario):
        super().__init__(usuario)

    def __str__(self) -> str:
        return (f"El usuario con nombre de usuario: '{self.usuario.nombre_usuario}' ya existe en el sistema, intenta iniciar sesión.")