from django import forms
from .models import Produto
class ProdutoForm(forms.ModelForm):
   class Meta:
        model = Produto
        fields = ['codigo', 'descricao', 'marca','quantidade_minima', 'quantidade', 'custo', 'preco', 'observacao'] # Campos do formulário'