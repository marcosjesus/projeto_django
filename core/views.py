"""
    print(dir(request))
    print(f'Metodo: {request.method}')
    print(f'header: {request.headers}')
    print(f"User-Agent: {request.headers['User-Agent']}")  # Pegar navegador e OS do Usuario
    print(f"User: {request.user}") # pegar o usuario logado na pagina
"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        status = 'Usuario não logado'
    else:
        status = 'Usuario logado'
    context = {
        'curso': 'Programação Web co Django Framwork',
        'outro': 'Vamos criar uma empresa',
        'status': status,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html charset=utf8', status=500)
