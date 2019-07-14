from django.db import models

## Cliente
class Carro(models.Model):
    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=25)

    def __str__(self):
        return self.modelo

class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    telefone1 = models.CharField(max_length=14)
    telefone2 = models.CharField(max_length=14)
    carro = models.ForeignKey(
        'Carro',
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.nome

## Serviços 
class Defeito(models.Model):
    tipo = models.CharField(max_length=25)
    descricao = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo

class Servico(models.Model):
    codigo = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)
    entrada = models.DateTimeField(auto_now_add=True, blank=True)
    saida = models.DateTimeField()
    finalizado = models.BooleanField()
    comentarios = models.TextField()

    def __str__(self):
        return self.codigo

class Operacao(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    comentarios = models.TextField()

    def __str__(self):
        return str(self.tipo) 

# Financeiro
class Pagamento(models.Model):
    efetuado = models.BooleanField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.valor)

class FormaDePagamento(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()

    def __str__(self):
        return self.tipo

class Saida(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tipo

## Colaboradores
class Funcionario(models.Model):
    nome = models.CharField(max_length=25)
    loggin = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo
    