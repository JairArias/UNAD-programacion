from core.clients import Cliente
from core.service import SalaReserva, EquipoAlquiler, Asesoria
from core.booking import Reserva
from core.utils import Logger
import sys

def simulate():
    print("=== SOFTWARE FJ SYSTEM START ===")
    
    # Datos maestros
    try:
        cliente_valido = Cliente("C001", "Margarita Rosa", "marga@mail.com")
        sala = SalaReserva("Conference Hall", 100)
        equipo = EquipoAlquiler("Projector 4K", 50)
        asesor = Asesoria("Software Architecture", 200)
    except Exception as e:
        print(f"Critical error initializing: {e}")
        sys.exit()

    # --- 10 OPERACIONES ---
    operaciones = [
        # 1. Éxito: Sala con limpieza
        lambda: Reserva(cliente_valido, sala, 4).procesar(limpieza=True),
        
        # 2. Error: Cliente con nombre corto
        lambda: Cliente("C002", "Jo", "jo@mail.com"),
        
        # 3. Éxito: Alquiler con seguro
        lambda: Reserva(cliente_valido, equipo, 2).procesar(seguro=True),
        
        # 4. Error: Alquiler con días negativos
        lambda: Reserva(cliente_valido, equipo, -5).procesar(),
        
        # 5. Éxito: Asesoría Premium
        lambda: Reserva(cliente_valido, asesor, 3).procesar(premium=True),
        
        # 6. Error: ID de cliente inválido (símbolos)
        lambda: Cliente("!!!", "Test User", "test@mail.com"),
        
        # 7. Éxito: Sala estándar
        lambda: Reserva(cliente_valido, sala, 2).procesar(limpieza=False),
        
        # 8. Error: Parámetro faltante o erróneo en cálculo
        lambda: sala.calcular_costo("muchas horas"),
        
        # 9. Éxito: Alquiler sin seguro
        lambda: Reserva(cliente_valido, equipo, 1).procesar(seguro=False),
        
        # 10. Error: Intento de reserva con cliente inexistente (None)
        lambda: Reserva(None, sala, 5).procesar()
    ]

    for i, op in enumerate(operaciones, 1):
        print(f"\nOperation #{i}:")
        try:
            resultado = op()
            print(f"Result: {resultado}")
        except Exception as e:
            # try/except/else/finally requerido
            print(f"Caught expected exception: {e}")
        else:
            print("Operation executed without errors.")
        finally:
            print("Cleaning up operation resources...")

    print("\n=== SIMULATION FINISHED. Check error_log.txt ===")

if __name__ == "__main__":
    simulate()
