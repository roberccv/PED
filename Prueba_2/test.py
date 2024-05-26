from figura import Figura
import unittest

#X_max , X_min , Y_max , Y_min
class TestFigura(unittest.TestCase):
    def test_area(self):
        fig = Figura()
        area = fig.area(10, 0, 3, 2)
        self.assertEqual(area, ((10-0)*(3-2)))

if __name__ == '__main__':
    unittest.main()