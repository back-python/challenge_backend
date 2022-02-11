from django.db import models
from datetime import datetime

# Create your models here.
class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=10)
    data = models.DateField(default=datetime.now, blank=True)

class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=10)
    data = models.DateField(default=datetime.now, blank=True)
