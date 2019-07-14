from  rest_framework import serializers
from . import models

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ('url', 'id', 'nome', 'telefone1', 'telefone2')

class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Carro
        fields = ('url', 'id', 'placa', 'modelo')

class DefeitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Defeito
        fields = ('url', 'id', 'tipo', 'descricao')

class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Servico
        fields = ('url', 'id', 
            'codigo', 'tipo', 'entrada', 'saida', 'finalizado', 'comentarios'
        )

class OperacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Operacao
        fields = ('url', 'id', 'tipo', 'valor', 'comentarios')

class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pagamento
        fields = ('url', 'id', 'efetuado', 'valor')

class FormaDePagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FormaDePagamento
        fields = ('url', 'id', 'tipo', 'valor')

class SaidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Saida
        fields = ('url', 'id', 'tipo', 'valor', 'data')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Funcionario
        fields = ('url', 'id', 'nome', 'loggin')

class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cargo
        fields = ('url', 'id', 'tipo')
