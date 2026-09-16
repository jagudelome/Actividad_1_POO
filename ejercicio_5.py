class numero:
    def __init__(self, primer_x, primer_y):
        self.suma = 0
        self.x = primer_x
        self.y = primer_y

    def calculo(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y

    def valor(self):
        print(f"el valor de la suma es: {self.suma}")

valor_suma = numero(primer_x= 20, primer_y=40)
valor_suma.calculo()
valor_suma.valor()

