class ErrorTasaUsura(Exception):

    def __init__(self, interes: float):
        super().__init__(f"Interés de {interes} supera tasa usura")




class ErrorMonto(Exception):
    def __init__(self, monto: int):
        super().__init__(f"El monto {monto}, no es superior a cero!")




class ErrorCuotaNegativa(Exception):
    def __init__(self, numero_cuotas: int):
        super().__init__(f"El total de cuotas igual a: {numero_cuotas}, no es superior a cero!")





