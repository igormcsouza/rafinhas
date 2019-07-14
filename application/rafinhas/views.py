from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ClienteView(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class CarroView(viewsets.ModelViewSet):
    queryset = models.Carro.objects.all()
    serializer_class = serializers.CarroSerializer

class DefeitoView(viewsets.ModelViewSet):
    queryset = models.Defeito.objects.all()
    serializer_class = serializers.DefeitoSerializer

class ServicoView(viewsets.ModelViewSet):
    queryset = models.Servico.objects.all()
    serializer_class = serializers.ServicoSerializer

class OperacaoView(viewsets.ModelViewSet):
    queryset = models.Operacao.objects.all()
    serializer_class = serializers.OperacaoSerializer

class PagamentoView(viewsets.ModelViewSet):
    queryset = models.Pagamento.objects.all()
    serializer_class = serializers.PagamentoSerializer

class FormaDePagamentoView(viewsets.ModelViewSet):
    queryset = models.FormaDePagamento.objects.all()
    serializer_class = serializers.FormaDePagamentoSerializer

class SaidaView(viewsets.ModelViewSet):
    queryset = models.Saida.objects.all()
    serializer_class = serializers.SaidaSerializer

class FuncionarioView(viewsets.ModelViewSet):
    queryset = models.Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer

class CargoView(viewsets.ModelViewSet):
    queryset = models.Cargo.objects.all()
    serializer_class = serializers.CargoSerializer

