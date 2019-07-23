from django.db import models
import datetime

from . import relacionamento, colaborador

class Transacao(models.Model):
    caracteristica = models.CharField(max_length=10)
    data = models.DateField(default=datetime.date.today)

    def findAllRetiradaByTransacao(self):
        return Retirada.objects.filter(transacao=self)
    def findAllRecebimentoByTransacao(self):
        return Pagamento.objects.filter(transacao=self)
    def __str__(self):
        return self.caracteristica + 's do dia ' + str(self.data)

class Retirada(models.Model):
    # Import ERROR
    # funcionario = models.ForeignKey(
    #     colaborador.Funcionario,
    #     on_delete=models.CASCADE,
    #     default=1
    # )
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True, blank=True)
    transacao = models.ForeignKey(
        Transacao,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.tipo + ' - ' + self.operador.nome

class Pagamento(models.Model):
    cliente = models.ForeignKey(
        relacionamento.Cliente,
        on_delete=models.CASCADE,
        default=1
    )
    efetuado = models.BooleanField()
    valor = models.FloatField(null=True) # Not necessary??
    transacao = models.ForeignKey(
        Transacao,
        on_delete=models.CASCADE,
        default=1 
    )

    def FindAllFormaDePagamentoByPagamento(self):
        return FormaDePagamento.objects.filter(pagamento=self)
    def FindTotalCost(self):
        valor = 0
        for f in self.FindAllFormaDePagamentoByPagamento():
            valor += f.valor
        self.valor = valor
    def __str__(self):
        return 'Valor de ' + str(self.valor) + '. Efetuado por ' + self.cliente.nome

class FormaDePagamento(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    pagamento = models.ForeignKey(
        Pagamento,
        on_delete=models.CASCADE,
        default=1 #Pagamento.objects.first().id
    )

    def __str__(self):
        return self.tipo