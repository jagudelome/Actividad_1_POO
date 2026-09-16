import math
class figura:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def longitud(self):
        return 2 * math.pi * self.radio

    def resultado(self):
        print(f"El area del circulo es: {self.area()}")
        print(f"La longitud del circulo es: {self.longitud()}")

numero = int(input("El radio es: "))
calculo = figura(numero)
calculo.resultado()

    