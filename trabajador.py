class trabajo:
    def __init__(self, horas, valor_h, retencion):
        self.horas = horas
        self.valor_h = valor_h
        self.retencion = retencion

    def c_salario_bruto(self):
        return self.horas * self.valor_h

    def c_retencion(self):
        salario_bruto = self.c_salario_bruto()
        return salario_bruto * (self.retencion / 100)

    def valor_neto(self):
        return self.c_salario_bruto() - self.c_retencion()

    def total(self):
        print(f"El salario bruto es: {self.c_salario_bruto()}")
        print(f"La retencion en fuente es: {self.c_retencion()}")
        print(f"El salario neto es: {self.valor_neto()}")

empleado = trabajo(horas=48, valor_h=5000, retencion=12.5)
empleado.total()


    
        