from core.utils import Logger
from core.base import ServiceUnavailableError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDING"

    def procesar(self, **opciones):
        try:
            costo = self.servicio.calcular_costo(self.duracion, **opciones)
            self.estado = "CONFIRMED"
            msg = f"SUCCESS: {self.cliente.nombre} booked {self.servicio.nombre} for ${costo}"
            Logger.log_event(msg)
            return msg
        except Exception as e:
            self.estado = "FAILED"
            Logger.log_error(f"Booking failed for {self.cliente.nombre}: {e}")
            # Encadenamiento de excepciones
            raise ServiceUnavailableError(f"Cannot complete booking: {e}") from e
