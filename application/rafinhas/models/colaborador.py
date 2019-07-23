from django.db import models

from . import financa

class Funcionario(models.Model):
    nome = models.CharField(max_length=25)
    loggin = models.CharField(max_length=25)
    papel = models.CharField(max_length=25, null=True)

    def findAllRetiradaByFuncionario(self):
        return financa.Retirada.objects.filter(funcionario=self)
    def __str__(self):
        return self.nome