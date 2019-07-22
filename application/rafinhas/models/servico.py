from django.db import models
import datetime

from . import relacionamento, financa, colaborador

class Operacao(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    comentarios = models.TextField(null=True)

    def __str__(self):
        return str(self.tipo)

class Servico(models.Model):
    codigo = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)
    carro = models.ForeignKey(
        relacionamento.Carro,
        on_delete=models.CASCADE,
        default=1
    )
    entrada = models.DateField(auto_now_add=True, blank=True)
    saida = models.DateField(default=datetime.date.today, null=True)
    finalizado = models.BooleanField()
    comentarios = models.TextField(null=True)
    pagamento = models.ForeignKey(
        financa.Pagamento,
        on_delete=models.CASCADE,
        null=True
    )
    operacao = models.ForeignKey(
        Operacao,
        on_delete=models.CASCADE,
        default=1 #Operacao.objects.first().id
    )
    operador = models.ForeignKey(
        colaborador.Funcionario,
        on_delete=models.CASCADE,
        default=1 #Funcionario.objects.first().id
    )

    # Deve haver mais um campo para vendedor

    def __str__(self):
        return self.codigo + ' - ' + self.tipo