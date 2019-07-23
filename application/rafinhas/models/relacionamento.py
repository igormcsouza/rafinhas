from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    telefone1 = models.CharField(max_length=14)
    telefone2 = models.CharField(max_length=14, null=True)

    def findCarroByCliente(self):
        return Carro.objects.filter(cliente=self)
    def __str__(self):
        return self.nome

class Carro(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    modelo = models.CharField(max_length=25)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        default=1 #Cliente.objects.first().id
    )

    def findDefeitoByCarro(self):
        return Defeito.objects.filter(carro=self)
    def __str__(self):
        return self.modelo

class Defeito(models.Model):
    tipo = models.CharField(max_length=25)
    descricao = models.TextField()
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE,
        default=1 #Carro.objects.first().id
    )

    def __str__(self):
        return self.tipo + ' no carro ' + self.carro.placa

class Imagem(models.Model):
    pass