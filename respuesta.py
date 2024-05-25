import datetime
class Respuesta:
    def respuesta_del_servidor(self, mensaje):
        if mensaje == b"Hora":
            return datetime.datetime.now().strftime("%H:%M:%S")
        else: pass