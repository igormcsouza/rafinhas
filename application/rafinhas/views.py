from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models.colaborador import *
from .models.financa import *
from .models.relacionamento import *
from .models.servico import *
from . import serializers

class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class CarroView(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = serializers.CarroSerializer

class DefeitoView(viewsets.ModelViewSet):
    queryset = Defeito.objects.all()
    serializer_class = serializers.DefeitoSerializer

class ServicoView(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = serializers.ServicoSerializer

class OperacaoView(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = serializers.OperacaoSerializer

class TransacaoView(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = serializers.TransacaoSerializer

class PagamentoView(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = serializers.PagamentoSerializer

class FormaDePagamentoView(viewsets.ModelViewSet):
    queryset = FormaDePagamento.objects.all()
    serializer_class = serializers.FormaDePagamentoSerializer

class RetiradaView(viewsets.ModelViewSet):
    queryset = Retirada.objects.all()
    serializer_class = serializers.RetiradaSerializer

class FuncionarioView(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer


