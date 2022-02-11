from rest_framework import viewsets
from movimentacoes.models import Receita, Despesa
from movimentacoes.serializer import ReceitaSerializer, DespesaSerializer

class ReceitasViewSet(viewsets.ModelViewSet):
    """ Listando todas as receitas """
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class DespesasViewSet(viewsets.ModelViewSet):
    """ Listando todas as despesas """
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
