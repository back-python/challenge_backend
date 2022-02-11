from rest_framework import serializers
from movimentacoes.models import Receita, Despesa
from movimentacoes.validators import *

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

    def validate(self, data):
        if not descricao_valida(data['descricao']):
            raise serializers.ValidationError({'nome','O campo da descrição não pode ficar em branco'})
        if not valor_valido(data['valor']):
            raise serializers.ValidationError({'valor','O campo do valor não pode ficar em branco'})
        if not data_valida(data['data']):
            raise serializers.ValidationError({'valor','O campo da data não pode ficar em branco'})

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

    def validate(self, data):
        if not descricao_valida(data['descricao']):
            raise serializers.ValidationError({'nome','O campo da descrição não pode ficar em branco'})
        if not valor_valido(data['valor']):
            raise serializers.ValidationError({'valor','O campo do valor não pode ficar em branco'})
        if not data_valida(data['data']):
            raise serializers.ValidationError({'valor','O campo da data não pode ficar em branco'})