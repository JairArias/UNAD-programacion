from abc import ABC, abstractmethod

# --- Excepciones Personalizadas ---
class SoftwareFJException(Exception):
    """Excepción base para el sistema Software FJ."""
    pass

class InvalidDataError(SoftwareFJException):
    """Se lanza cuando los datos de entrada son incorrectos."""
    pass

class ServiceUnavailableError(SoftwareFJException):
    """Se lanza cuando un servicio no puede procesarse."""
    pass

# --- Clase Abstracta Base ---
class EntidadBase(ABC):
    @abstractmethod
    def obtener_detalles(self):
        """Obliga a todas las entidades a tener una descripción."""
        pass
