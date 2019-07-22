from django.db import models
import datetime

from . import relacionamento, colaborador

class Transacao(models.Model):
    caracteristica = models.CharField(max_length=10)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.caracteristica + 's do dia ' + str(self.data)

class Retirada(models.Model):
    operador = models.ForeignKey(
        colaborador.Funcionario,
        on_delete=models.CASCADE,
        default=1
    )
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True, blank=True)
    transacao = models.ForeignKey(
        Transacao,
        on_delete=models.CASCADE,
        default=1 #Transacao.objects.first().id
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
    valor = models.FloatField(null=True)
    transacao = models.ForeignKey(
        Transacao,
        on_delete=models.CASCADE,
        default=1 
    )

    def __str__(self):
        return 'Valor de ' + str(self.valor) + '. Efetuado por ' + self.cliente.name

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