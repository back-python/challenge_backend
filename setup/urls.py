from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from movimentacoes.views import ReceitasViewSet, DespesasViewSet

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
