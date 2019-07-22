from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=25)
    loggin = models.CharField(max_length=25)
    papel = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.nome