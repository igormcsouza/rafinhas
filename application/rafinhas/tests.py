from django.test import TestCase
from .models import *

class Fluxo(TestCase):
    def novoCliente():
        Cliente.objects.all()
        joao = Cliente(nome="Joao Cardoso", telefone1='85998754774')
        joao.save()
        print(joao.id)
        
        sandero = Carro(placa='CDE7847', modelo='Sandeiro')
        sandero.save()
        sandero.cliente = joao
        print(sandero.cliente)
        sandero.modelo='Sandero'

        arranhao = Defeito(tipo='Arranhao', descricao='Na parte superior esquerda', carro=sandero)

        servico = Servico()
        servico.codigo='ASW123'
        servico.tipo='Lavagem'
        servico.finalizado=False
        servico.comentarios='Vai pegar no fim do dia'

        dede = Funcionario(nome='Dede', loggin='1', papel='Operador')
        servico.operador = dede
        dede.save()

        sandero.save()
        arranhao.save()
        
        lavagem = Operacao(tipo='Lavagem', valor=10.00)
        lavagem.save()

        servico.operacao=lavagem
        servico.save()
        print(servico)

        servico.carro=sandero
        print(Defeito.objects.filter(carro=servico.carro))

