class Familia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def c_alber(self):
        return (2 / 3) * self.edad_juan
    def c_ana(self):
        return (4 / 3) * self.edad_juan
    def c_mama(self):
        return self.edad_juan + self.c_ana() + self.c_alber()

    def mostrar(self):
        print(f"Edad de Juan: {self.edad_juan}")
        print(f"Edad de Alberto: {self.c_alber()}")
        print(f"Edad de Ana: {self.c_ana()}")
        print(f"Edad de la mama: {self.c_mama()}")

edad_juan = int(input("Ingrese la edad de Juan: "))

familia = Familia(edad_juan)
familia.mostrar()