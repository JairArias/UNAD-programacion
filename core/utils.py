import datetime

class Logger:
    @staticmethod
    def log_error(mensaje):
        """Registra errores en el archivo log con marca de tiempo."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("error_log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] [ERROR] {mensaje}\n")

    @staticmethod
    def log_event(mensaje):
        """Registra eventos exitosos en el archivo log."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("error_log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] [EVENTO] {mensaje}\n")
