from django import forms
from .models import vendas, item_venda
class VendaForm(forms.ModelForm):
    class Meta:
        model = vendas
        fields = ['nome_cliente']
class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = item_venda
        fields = ['produto', 'quantidade']