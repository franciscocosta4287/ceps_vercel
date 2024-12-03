from django.urls import path
from .views import consulta_cep, salvar_cep, consulta_cep_ajax, relatorio_cep

urlpatterns = [
    path('consulta/', consulta_cep, name='consulta_cep'),
    path('salvar/', salvar_cep, name='salvar_cep'),
    path('relatorio/', relatorio_cep, name='relatorio_cep'),
    path('consulta-cep/', consulta_cep_ajax, name='consulta_cep_ajax'),
]