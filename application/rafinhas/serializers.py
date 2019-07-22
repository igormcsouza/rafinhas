from  rest_framework import serializers
from .models.colaborador import *
from .models.financa import *
from .models.relacionamento import *
from .models.servico import *

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('url', 'id', 'nome', 'telefone1', 'telefone2')

class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ('url', 'id', 'placa', 'modelo', 'cliente')

class DefeitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Defeito
        fields = ('url', 'id', 'tipo', 'descricao', 'carro')

class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servico
        fields = ('url', 'id', 
            'codigo', 'tipo', 'carro', 'entrada', 'saida', 'finalizado', 
            'comentarios', 'pagamento', 'operacao', 'operador'
        )

class OperacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operacao
        fields = ('url', 'id', 'tipo', 'valor', 'comentarios')

class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transacao
        fields = ('url', 'id', 'caracteristica', 'data')

class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pagamento
        fields = ('url', 'id', 'efetuado', 'valor', 'transacao')

class FormaDePagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaDePagamento
        fields = ('url', 'id', 'tipo', 'valor', 'pagamento')

class RetiradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Retirada
        fields = ('url', 'id', 'tipo', 'valor', 'data', 'transacao')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('url', 'id', 'nome', 'loggin', 'papel')
