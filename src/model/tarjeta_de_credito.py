from src.model.compra import Compra


class TarjetaDeCredito:

    def __init__(self, tasa_interes: float, cupo_disponible: float):
        self.compras = list[Compra]

    def registrar_compra(self, compra: Compra):
        pass

    def calcular_total_interes(self)-> float:
        pass