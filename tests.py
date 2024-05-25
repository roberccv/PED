import unittest, datetime
from respuesta import Respuesta

class TestRespuesta(unittest.TestCase):
    def test_respuesta_Hora(self):
        solucion = Respuesta()
        contestacion_servidor = solucion.respuesta_del_servidor(b"Hora")
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        self.assertEqual(contestacion_servidor, hora)

    def test_respuesta_Fecha(self):
        solucion = Respuesta()
        contestacion_servidor = solucion.respuesta_del_servidor(b"Fecha")
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        self.assertEqual(contestacion_servidor, fecha)
if __name__ == '__main__':
    unittest.main()