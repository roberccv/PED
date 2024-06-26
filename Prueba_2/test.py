from figura import Figura
import unittest

#X_max , X_min , Y_max , Y_min
class TestFigura(unittest.TestCase):
    def test_area(self):
        fig = Figura()
        area = fig.area(10, 0, 3, 2)
        self.assertEqual(area, ((10-0)*(3-2)))
    
    def test_perimetro(self):
        fig = Figura()
        perimetro = fig.perimetro(10, 0, 3, 2)
        self.assertEqual(perimetro, ((10-0)*2 + (3-2)*2))
    
    def test_punto_medio(self):
        fig = Figura()
        punto_medio = fig.punto_medio(10, 0, 3, 2)
        self.assertEqual(punto_medio, ((10+0)/2, (3+2)/2))


if __name__ == '__main__':
    unittest.main()