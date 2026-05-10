from core.base import EntidadBase, InvalidDataError
from core.utils import Logger

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email):
        self.__id_cliente = None  # Privado
        self.__nombre = None      # Privado
        self.email = email        # Público
        
        # Validación mediante setters
        self.id_cliente = id_cliente
        self.nombre = nombre

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        if not str(valor).isalnum():
            Logger.log_error(f"ID inválido: {valor}")
            raise InvalidDataError("El ID del cliente debe ser alfanumérico.")
        self.__id_cliente = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip()) < 3:
            Logger.log_error(f"Nombre muy corto: {valor}")
            raise InvalidDataError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor

    def obtener_detalles(self):
        return f"Client: {self.nombre} (ID: {self.id_cliente})"
