from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return render(request, 'simples.html',{})

def dinamico(request):
    
    return render(request, 'dinamico.html', {} )

def ejemplo(request):
    return render(request, 'ejemplo.html', {})

def base(request):
    return render(request, 'base.html', {})
    