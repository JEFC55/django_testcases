from django.db import models

# Create your models here.
from django.db import models  

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    rg= models.CharField(max_length=12, blank=True, null=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    titulo_eleitoral = models.CharField(max_length=12, blank=True, null=True)
    escolaridade = models.CharField(max_length=20, blank=True, null=True)
    profissao = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Remove qualquer formatação do CPF antes de salvar
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome