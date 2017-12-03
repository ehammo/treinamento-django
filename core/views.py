from django.shortcuts import render
from django.http import Http404
from .models import Livro, Editora
# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

def livros(request):
    livros = Livro.objects.all()
    if not livros:
        livros = None
    return render(
        request,
        'livros.html',
        {
            "Livros":livros,
        }
    )

def editora(request, editoraId):
    editora = Editora.objects.get(id=editoraId)
    livros = Livro.objects.get_queryset().filter(editora=editoraId)
    if not editora:
         raise Http404('Editora não encontrada')
    return render(
        request,
        'editora.html',
        {
            "Editora":editora,
            "Livros":livros,
        }
    )