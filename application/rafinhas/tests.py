from django.test import TestCase
from .models.colaborador import *
from .models.financa import *
from .models.relacionamento import *
from .models.servico import *

class Fluxo(TestCase):
    def test_novoCliente(self):
        print("\n\nIniciando os Testes de Fluxo...")

        # Para propósitos de teste
        print("Um novo funcionário é cadastrado...")
        flavio = Funcionario(nome='Flavio', loggin='1', papel='Operador')
        flavio.save()
        print("Novo funcionario: {0}".format(flavio))

        print("Uma nova operação é registrada...")
        lavagem = Operacao(tipo='Lavagem', valor=10.00)
        lavagem.save()
        print("Nova operacao: {0}".format(lavagem))

        print("Uma outra operação é registrada...")
        troca = Operacao(tipo='Troca de Óleo', valor=20.00)
        troca.save()
        print("Nova operacao: {0}".format(troca))

        print("Criando uma nova transação...")
        hoje = Transacao()
        hoje.caracteristica = 'Entrada'
        hoje.save()
        print("Nova operacao: {0}".format(hoje))

        # Início do fluxo -----------------------------------------------------
        print("\n\nCliente chega no lava jato...")
        antonio = Cliente(nome="Antonio Duarte", telefone1='85987474111')
        antonio.save()
        print("ID do novo cliente: {0}".format(antonio.id))
        
        print("Cliente cadastra seu carro...")
        renault = Carro(placa='CDE7847', modelo='Renault')
        renault.cliente = antonio
        renault.save()
        print("Novo carro: {0}".format(renault))
        print("Cliente do Novo carro: {0}".format(renault.cliente))

        print("Cliente mostra os defeitos aparentes no carro...")
        risco = Defeito(tipo='Risco', descricao='Na parte superior esquerda', carro=renault)
        risco.save()

        print("O cadastro do serviço é efetuado pelo operador...")
        servico = Servico()
        servico.codigo='ASW123'
        servico.tipo='Lava Jato'
        servico.carro=renault
        servico.finalizado=False
        servico.comentarios='Vai pegar no fim do dia'
        servico.operador = flavio
        servico.save()

        # Incluindo 2 tipos de operacao
        servico.operacao.add(lavagem)
        servico.operacao.add(troca)
        servico.save()
        print("Novo Servico: {0}".format(servico))

        print("Alguns detalhes do serviço podem ser vistos pela ADM...")
        print("Placa do carro: {0}".format(servico.carro.placa))
        print("Pesquisa de Defeitos no carro do servico atual: {0}".format(
            Defeito.objects.filter(carro=servico.carro)
        ))
        print("Operações que serão realizadas: {0}".format(servico.operacao))

        # Erro aqui, o cliente pode pedir mais de uma operação
        print("O cliente chega para buscar o carro e pergunta o valor do serviço...")
        valor = 0
        for i in servico.operacao.all():
            valor += i.valor
        print("O custo foi {0}".format(valor))

        print("O cliente então efetua o pagamento...")
        pag = Pagamento()
        pag.efetuado=True
        pag.valor = 0
        pag.transacao = hoje # O certo mesmo é procurar pela transacao de hoje
        pag.save()

        # Não seria melhor ter um campo no pagamento que armazena todas as formas de pagamento???
        print("Ele efetua metade no cartao e a outra em dinheiro...")
        cartao = FormaDePagamento()
        cartao.pagamento = pag
        cartao.valor = valor/2
        cartao.tipo = 'Cartão de Crédito'
        cartao.save()

        dinheiro = FormaDePagamento()
        dinheiro.pagamento = pag
        dinheiro.valor = valor/2
        dinheiro.tipo = 'Dinheiro'
        dinheiro.save()

        pag.valor=cartao.valor+dinheiro.valor
        pag.save()

        if(pag.valor == valor):
            servico.finalizado = True
        print("O servico foi finalizado? {0}".format(servico.finalizado))

        print("O fluxo foi finalizado com sucesso! 2 Erros de Banco para concertar!!")

        

