from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf','nome', 'telefone','email','titulo_eleitoral', 'escolaridade', 'profissao', 'rg']