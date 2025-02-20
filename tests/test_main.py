import pytest

from src.model.tarjeta_de_credito import TarjetaDeCredito
from src.model.compra import Compra
from src.model.errors import ErrorTasaUsura
from src.model.errors import ErrorMonto
from src.model.errors import ErrorCuotaNegativa


def test_caso_36_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.1, 1000000)
    compra: Compra = Compra(200000, 3.1, 36)
    tarjeta_de_credito.registrar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 134726.53

def test_caso_24_cuotas():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(3.4, 25000)
    compra: Compra = Compra(850000, 3.4, 24)
    tarjeta_de_credito.registrar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 407059.97

def test_caso_tasa_cero():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(0, 2000000)
    compra: Compra = Compra(480000, 0, 48)
    tarjeta_de_credito.registrar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0


def test_caso_tasa_usura():
    with pytest.raises(ErrorTasaUsura):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(12.5, 30000)
        compra: Compra = Compra(50000, 12.5, 60)
        tarjeta_de_credito.registrar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()
        #raise ErrorTasaUsura(12.5)


def test_caso_cuota_unica():
    tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(2.4, 200)
    compra: Compra = Compra(90000, 2.4, 1)
    tarjeta_de_credito.registrar_compra(compra)
    total_interes = tarjeta_de_credito.calcular_total_interes()
    assert total_interes == 0


def test_caso_monto_invalido():
    with pytest.raises(ErrorMonto):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(2.4, 9800)
        compra: Compra = Compra(0, 2.4, 60)
        tarjeta_de_credito.registrar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()
        #raise ErrorMonto(0)



def test_caso_cuota_negativa():
    with pytest.raises(ErrorCuotaNegativa):
        tarjeta_de_credito: TarjetaDeCredito = TarjetaDeCredito(1, 40998)
        compra: Compra = Compra(50000, 1, -10)
        tarjeta_de_credito.registrar_compra(compra)
        total_interes = tarjeta_de_credito.calcular_total_interes()
        #raise ErrorCuotaNegativa(-10)






