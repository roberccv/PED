class Figura:

    def area(self, X_max, X_min, Y_max, Y_min):
        return ((X_max - X_min) * (Y_max - Y_min))
    def perimetro(self, X_max, X_min, Y_max, Y_min):
        return ((X_max - X_min) * 2 + (Y_max - Y_min) * 2)
        
