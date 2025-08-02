from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class vendas(models.Model):
    num_venda = models.AutoField(primary_key=True)
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    total_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.num_venda} - Cliente: {self.cliente.nome}"

class item_venda(models.Model):
    venda = models.ForeignKey(vendas, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.descricao} (Venda {self.venda.num_venda})"