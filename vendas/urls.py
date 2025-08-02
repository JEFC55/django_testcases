from django.urls import path
from vendas.views import lista_vendas , criar_venda, editar_venda, excluir_venda, excluir_item_venda, imprimir_venda
urlpatterns = [
    path('', lista_vendas, name='lista_vendas'),
    path('nova/', criar_venda, name='criar_venda'),
    path('editar/<int:venda_id>/', editar_venda, name='editar_venda'),
    path('excluir/<int:venda_id>/', excluir_venda, name='excluir_venda'),
    path('excluir-item/<int:item_id>/', excluir_item_venda, name='excluir_item_venda'),  
    path('imprimir/<int:venda_id>/', imprimir_venda, name='imprimir_venda'), 
 ]