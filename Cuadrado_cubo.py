class calculo:
    def __init__(self, numero):
        self.numero = numero

    def cuadrado(self):
        return self.numero ** 2

    def cubo(self):
        return self.numero ** 3

    def mostrar(self):
        print(f"El cuadrado es: {self.cuadrado()}")
        print(f"El cubo es: {self.cubo()}")

Numero = int(input("Numero: "))
c_numero = calculo(Numero)
c_numero.mostrar()


