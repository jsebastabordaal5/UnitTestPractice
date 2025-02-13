class TarjetaCredito:

    def __init__(self, N: int, P: int, I: float):
        self.N = N
        self.P = P
        self.I = I

    def cuota_mensual(self):
        if self.I == 0:
            return self.P / self.N
        C = (self.P * self.I)/(1-(1+self.I)**-self.N)
        return C

    def total_intereses(self):
        TI = (self.cuota_mensual() * self.N) - self.P
        return TI

a1 = TarjetaCredito(48, 850000, 3.4)
print(a1.total_intereses())



