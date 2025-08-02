from django.urls import path
from . import views

urlpatterns = [path('', views.lista_produtos, name='lista_produtos'),
               path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
               path('consultar/<str:codigo>/', views.consultar_produto, name='consultar_produto'),
               path('excluir/<str:codigo>/', views.excluir_produto, name='excluir_produto'),
               path('editar/<str:codigo>/', views.cadastrar_produto, name='editar_produto'),
               ]