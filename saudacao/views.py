from django.shortcuts import render
from datetime import datetime

def saudacao(request):
    saudacao="Olá mundo!"
    return render(request, 'saudacao.html', {'saudacao': saudacao})

# Create your views here
