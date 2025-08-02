from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('consultar_cliente/<str:cpf>/', views.consultar_cliente, name='consultar_cliente'),
    path('buscar_nome/', views.buscar_nome, name='buscar_nome'),
    path('excluir_cliente/<str:cpf>/', views.excluir_cliente, name='excluir_cliente'),
]