from django.test import TestCase
from .models import *

class Fluxo(TestCase):
    def test_novoCliente(self):
        print("Iniciando os Testes...")
        antonio = Cliente(nome="Antonio Duarte", telefone1='85987474111')
        antonio.save()
        print("ID do novo cliente: {0}".format(antonio.id))
        
        renault = Carro(placa='CDE7847', modelo='Renault')
        renault.cliente = antonio
        renault.save()
        print("Novo carro: {0}".format(renault))
        print("Cliente do Novo carro: {0}".format(renault.cliente))

        risco = Defeito(tipo='Risco', descricao='Na parte superior esquerda', carro=renault)
        risco.save()

        flavio = Funcionario(nome='Flavio', loggin='1', papel='Operador')
        flavio.save()
        print("Novo funcionario: {0}".format(flavio))

        lavagem = Operacao(tipo='Lavagem', valor=10.00)
        lavagem.save()
        print("Nova operacao: {0}".format(lavagem))

        servico = Servico()
        servico.codigo='ASW123'
        servico.tipo='Lavagem'
        servico.carro=renault
        servico.finalizado=False
        servico.comentarios='Vai pegar no fim do dia'
        servico.operador = flavio
        servico.operacao=lavagem
        servico.save()
        print("Novo Servico: {0}".format(servico))

        print("Placa do carro: {0}".format(servico.carro.placa))
        print("Pesquisa de Defeitos no carro do servico atual: {0}".format(
            Defeito.objects.filter(carro=servico.carro)
        ))

