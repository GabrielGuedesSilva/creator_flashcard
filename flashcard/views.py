from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView (TemplateView):
    template_name = 'flashcard/home.html'

def escolher_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/escolher_grupo.html'
        )
def tipo_criacao_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/escolher_tipo_flashcard.html'
        )

def criar_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/criar_flashcard.html'
        )

def revisao(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/revisao/pratica.html'
        )

def criar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/criar_grupo.html'
        )

def visualizar_grupos_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_grupos.html'
        )

def visualizar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_um_grupo.html'
        )

def excluir_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/excluir_grupo.html'
        )

def editar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/editar_grupo.html'
        )


class Login (LoginView):
    template_name = 'flashcard/usuarios/login.html'

def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/usuarios/cadastro_usuario.html'
        )

class Logout (LogoutView):
    template_name = 'flashcard/usuarios/logout.html'

# FLASHCARDS
def visualizar_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/visualizar_flashcard.html'
        )

def editar_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/editar_flashcard.html'
        )

def excluir_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/excluir_flashcard.html'
        )


