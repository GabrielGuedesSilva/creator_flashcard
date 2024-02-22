from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from flashcard.forms import RegisterForm


class HomeView (TemplateView):
    template_name = 'flashcard/home.html'


class Login (LoginView):
    template_name = 'flashcard/usuarios/login.html'
    next_page = reverse_lazy('flashcard:home')


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

            return redirect('flashcard:home')

