from re import search
from django.contrib import admin
from movimentacoes.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'data')
    list_filter = ('data',)
    list_per_page = 50
    ordering = ('data',)

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'data')
    list_filter = ('data',)
    list_per_page = 50
    ordering = ('data',)

admin.site.register(Receita, Receitas)
admin.site.register(Despesa, Despesas)
