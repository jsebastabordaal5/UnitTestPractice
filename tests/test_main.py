import pytest

from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.model.compra import Compra

def test_caso_36_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    compra: Compra = Compra(200000, 3.1, 36)
    tarjeta_de_credito.registrar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53

def test_caso_24_cuotas():
    pass