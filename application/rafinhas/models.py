from django.db import models
import datetime

## Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    telefone1 = models.CharField(max_length=14)
    telefone2 = models.CharField(max_length=14, null=True)

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

## Serviços
class Financas(models.Model):
    caracteristica = models.CharField(max_length=10)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.caracteristica + ' do dia ' + str(self.data)

class Pagamento(models.Model):
    efetuado = models.BooleanField()
    valor = models.FloatField(null=True)
    financas = models.ForeignKey(
        Financas,
        on_delete=models.CASCADE,
        default=1 #Financas.objects.first().id
    )

    def __str__(self):
        return 'Valor de ' + str(self.valor) 

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

class Operacao(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    comentarios = models.TextField(null=True)

    def __str__(self):
        return str(self.tipo) 

# Financeir0
class Retirada(models.Model):
    tipo = models.CharField(max_length=25)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True, blank=True)
    financas = models.ForeignKey(
        Financas,
        on_delete=models.CASCADE,
        default=1 #Financas.objects.first().id
    )

    def __str__(self):
        return self.tipo

## Colaboradores
class Funcionario(models.Model):
    nome = models.CharField(max_length=25)
    loggin = models.CharField(max_length=25)
    papel = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    codigo = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25)
    carro = models.ForeignKey(
        Carro,
        on_delete=models.CASCADE,
        default=1
    )
    entrada = models.DateField(auto_now_add=True, blank=True)
    saida = models.DateField(default=datetime.date.today, null=True)
    finalizado = models.BooleanField()
    comentarios = models.TextField(null=True)
    pagamento = models.ForeignKey(
        Pagamento,
        on_delete=models.CASCADE,
        null=True
    )
    operacao = models.ForeignKey(
        Operacao,
        on_delete=models.CASCADE,
        default=1 #Operacao.objects.first().id
    )
    operador = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        default=1 #Funcionario.objects.first().id
    )

    # Deve haver mais um campo para vendedor

    def __str__(self):
        return self.codigo + ' - ' + self.tipo
    