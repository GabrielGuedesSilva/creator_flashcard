from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from flashcard.forms import RegisterForm, FlashcardForm


class HomeView (TemplateView):
    template_name = 'flashcard/home.html'

@login_required
def escolher_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/escolher_grupo.html'
        )

@login_required()
def tipo_criacao_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/escolher_tipo_flashcard.html'
        )
@login_required
def criar_flashcard(request):
    if request.method == 'GET':

        form = FlashcardForm()

        context = {
            'form': form
        }

        return render(
            request,
            'flashcard/criar_flashcard.html',
            context
        )
@login_required
def revisao(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/revisao/pratica.html'
        )
@login_required
def criar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/criar_grupo.html'
        )
@login_required
def visualizar_grupos_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_grupos.html'
        )
@login_required
def visualizar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_um_grupo.html'
        )
@login_required
def excluir_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/excluir_grupo.html'
        )
@login_required
def editar_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/editar_grupo.html'
        )


class Login (LoginView):
    template_name = 'flashcard/usuarios/login.html'
    success_url = reverse_lazy('flashcard:home')

class Logout (LogoutView):
    template_name = 'flashcard/usuarios/logout.html'

def cadastrar_usuario(request):
    if request.method == 'GET':

        form = RegisterForm()

        context = {
            'form': form
        }

        return render(
            request,
            'flashcard/usuarios/cadastro_usuario.html',
            context
        )

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect(
                redirect_to=reverse_lazy('flashcard:home')
            )

# FLASHCARDS
@login_required
def visualizar_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/visualizar_flashcard.html'
        )
@login_required
def editar_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/editar_flashcard.html'
        )
@login_required
def excluir_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/excluir_flashcard.html'
        )


