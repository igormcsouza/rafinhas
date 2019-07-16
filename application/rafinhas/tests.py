from django.test import TestCase
from . import models

class Fluxo(TestCase):
    def novoCliente():
        cliente = models.Cliente(
            nome="Sergio Mouro", 
            telefone1="85 987451369", 
            telefone2="85 999763258"
        )
        cliente.save()
        carro = models.Carro(placa="DEW8733", modelo="CHEVROLET", cliente=cliente)
        carro.save()
