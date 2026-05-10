from abc import abstractmethod
from core.base import EntidadBase, InvalidDataError
from core.utils import Logger

class Servicio(EntidadBase):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad, **kwargs):
        """Método polimórfico para cálculo de costos."""
        pass

class SalaReserva(Servicio):
    def calcular_costo(self, horas, limpieza=False):
        # Sobrecarga: costo extra por limpieza
        total = self.precio_base * horas
        if limpieza: total += 50
        return total

    def obtener_detalles(self):
        return f"Service: Room Booking ({self.nombre})"

class EquipoAlquiler(Servicio):
    def calcular_costo(self, dias, seguro=True):
        if dias <= 0: raise InvalidDataError("Days must be positive.")
        total = self.precio_base * dias
        return total * 1.15 if seguro else total # 15% seguro

    def obtener_detalles(self):
        return f"Service: Equipment Rental ({self.nombre})"

class Asesoria(Servicio):
    def calcular_costo(self, horas, premium=False):
        factor = 1.5 if premium else 1.0
        return (self.precio_base * horas) * factor

    def obtener_detalles(self):
        return f"Service: Specialized Consulting ({self.nombre})"
