from  rest_framework import serializers
from . import models

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ('url', 'id', 'nome', 'telefone1', 'telefone2')

class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Carro
        fields = ('url', 'id', 'placa', 'modelo', 'cliente')

class DefeitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Defeito
        fields = ('url', 'id', 'tipo', 'descricao', 'carro')

class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Servico
        fields = ('url', 'id', 
            'codigo', 'tipo', 'carro', 'entrada', 'saida', 'finalizado', 
            'comentarios', 'pagamento', 'operacao', 'operador'
        )

class OperacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Operacao
        fields = ('url', 'id', 'tipo', 'valor', 'comentarios')

class FinancasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Financas
        fields = ('url', 'id', 'caracteristica', 'data')

class PagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Pagamento
        fields = ('url', 'id', 'efetuado', 'valor', 'financas')

class FormaDePagamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FormaDePagamento
        fields = ('url', 'id', 'tipo', 'valor', 'pagamento')

class RetiradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Retirada
        fields = ('url', 'id', 'tipo', 'valor', 'data', 'financas')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Funcionario
        fields = ('url', 'id', 'nome', 'loggin', 'papel')
