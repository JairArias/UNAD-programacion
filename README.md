# Sistema de Gestión de Mantenimiento - Software FJ
**Estudiante:** John Jairo Pico  
**Curso:** Programación (Ingeniería de Sistemas - UNAD)

## 📝 Descripción del Proyecto
Este sistema simula la gestión de servicios técnicos en una empresa de tecnología. Permite registrar clientes y procesar diferentes tipos de servicios (Reserva de salas, Alquiler de equipos y Asesorías) validando reglas de negocio específicas.

## 🚀 Funcionalidades
El programa ejecuta una simulación de **10 operaciones** que demuestran:
- Manejo de herencia y polimorfismo.
- Validación de errores (por ejemplo, intentar alquilar un equipo sin stock).
- Generación de un archivo de registro de errores (`error_log.txt`).
- Resumen final de la jornada con estadísticas de éxito y fallo.

## 🛠️ Estructura del Repositorio
- `main.py`: Punto de entrada que ejecuta la simulación.
- `core/`: Carpeta que contiene la lógica modular (base, servicios, clientes y utilidades).
- `.gitignore`: Configuración para evitar subir archivos temporales de IntelliJ.
- `error_log.txt`: Registro detallado de incidentes durante la ejecución.

## 💻 Instrucciones de Ejecución
Para correr el programa, asegúrate de tener instalado Python 3 y ejecuta:
```bash
python main.py