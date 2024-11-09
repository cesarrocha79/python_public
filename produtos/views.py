from django.shortcuts import render, redirect
from django.http import HttpResponse


def produtos(request):
    return render(request, 'produtos.html')
