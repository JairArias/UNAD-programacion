from core.clients import Cliente
from core.services import SalaReserva, EquipoAlquiler, Asesoria
from core.bookings import Reserva
from core.base import SoftwareFJException
from core.utils import Logger

def ejecutar_simulacion():
    print("=== INICIANDO SIMULACIÓN DE 10 OPERACIONES - SOFTWARE FJ ===")

    # Lista para almacenar los resultados y mostrar al final
    operaciones_realizadas = []

    # --- DEFINICIÓN DE LAS 10 OPERACIONES ---
    # Usamos funciones lambda para ejecutarlas una por una en el ciclo
    pruebas = [
        # 1. REGISTRO VÁLIDO: Cliente correcto
        ("Registro Cliente", lambda: Cliente("C101", "John Jairo Pico", "john@mail.com")),

        # 2. REGISTRO INVÁLIDO: Cliente con nombre muy corto (Falla validación)
        ("Registro Cliente Inválido", lambda: Cliente("C102", "Jo", "error@mail.com")),

        # 3. CREACIÓN CORRECTA: Servicio de Sala
        ("Creación Servicio Sala", lambda: SalaReserva("Sala de Juntas Global", 150)),

        # 4. CREACIÓN INCORRECTA: Alquiler con días negativos (Falla lógica)
        ("Creación Servicio Erróneo", lambda: EquipoAlquiler("Laptop Dell", 50).calcular_costo(-5)),

        # 5. RESERVA EXITOSA: Cliente + Sala + Limpieza
        ("Reserva Exitosa", lambda: Reserva(
            Cliente("C103", "Margarita Rosa", "marga@mail.com"),
            SalaReserva("Auditorio", 200), 5
        ).procesar(limpieza=True)),

        # 6. RESERVA FALLIDA: Parámetros faltantes (Simulación de error de cálculo)
        ("Reserva Fallida", lambda: SalaReserva("Sala VIP", 100).calcular_costo("muchas horas")),

        # 7. REGISTRO INVÁLIDO: ID de cliente con símbolos prohibidos
        ("Registro ID Inválido", lambda: Cliente("ID-###-!", "Usuario Error", "test@mail.com")),

        # 8. RESERVA EXITOSA: Alquiler de equipo con seguro
        ("Reserva Exitosa Equipo", lambda: Reserva(
            Cliente("C105", "Andrés Pérez", "andres@mail.com"),
            EquipoAlquiler("Cámara 4K", 80), 3
        ).procesar(seguro=True)),

        # 9. RESERVA FALLIDA: Intento de reserva con objeto nulo (Error grave)
        ("Reserva Error Crítico", lambda: Reserva(None, None, 0).procesar()),

        # 10. RESERVA EXITOSA: Asesoría Especializada Premium
        ("Reserva Asesoría", lambda: Reserva(
            Cliente("C106", "Claudia López", "claudia@mail.com"),
            Asesoria("Consultoría IT", 300), 2
        ).procesar(premium=True)),
    ]

    # --- EJECUCIÓN CONTROLADA ---
    for i, (nombre_op, accion) in enumerate(pruebas, 1):
        print(f"\n>>> EJECUTANDO OPERACIÓN #{i}: {nombre_op}")
        try:
            # Intentamos ejecutar la operación
            resultado = accion()
            print(f"ESTADO: Completada exitosamente.")
            print(f"DETALLE: {resultado}")
            operaciones_realizadas.append(f"Op {i}: ÉXITO")

        except Exception as e:
            # BLOQUE TRY/EXCEPT/ELSE/FINALLY REQUERIDO
            print(f"ESTADO: Error capturado de forma profesional.")
            print(f"ERROR: {e}")
            # El logger ya se llama dentro de las clases, pero aquí reforzamos
            Logger.log_error(f"Operación {i} falló: {e}")
            operaciones_realizadas.append(f"Op {i}: FALLO CONTROLADO")

        else:
            # Se ejecuta si no hubo ninguna excepción
            Logger.log_event(f"Operación {i} ({nombre_op}) finalizada sin errores.")

        finally:
            # Siempre se ejecuta, garantiza la continuidad
            print(f"INFO: El sistema Software FJ permanece estable y activo.")

    # Resumen final
    print("\n" + "="*40)
    print("RESUMEN DE LA JORNADA")
    print("="*40)
    for res in operaciones_realizadas:
        print(res)
    print("="*40)
    print("Simulación terminada. Revise 'error_log.txt' para el historial técnico.")

if __name__ == "__main__":
    ejecutar_simulacion()
