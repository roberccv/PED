import datetime
class Respuesta:
    def respuesta_del_servidor(self, mensaje):
        if not isinstance(mensaje, bytes):
            raise TypeError("El mensaje debe ser de tipo bytes")
        elif mensaje == b"Hora":
            return datetime.datetime.now().strftime("%H:%M:%S")
        elif mensaje == b"Fecha":
            return datetime.datetime.now().strftime("%Y-%m-%d")
        else: return "ERROR"