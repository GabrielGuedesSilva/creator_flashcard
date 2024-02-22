from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from flashcard.forms import GrupoFlashcardForm
from flashcard.models import GrupoFlashcard


@login_required
def criar_grupo_flashcard(request):
    if request.method == 'GET':

        form = GrupoFlashcardForm()

        context = {
            'form': form
        }

        return render(
            request,
            'flashcard/grupos_flashcard/criar_grupo.html',
            context
        )

    if request.method == 'POST':
        form = GrupoFlashcardForm(request.POST)

        if form.is_valid():
            grupo_flashcard = GrupoFlashcard(**form.cleaned_data)
            grupo_flashcard.usuario_pertencente = request.user
            grupo_flashcard.save()
            return redirect('flashcard:visualizar_grupo_flashcard', tema=grupo_flashcard.tema)


@login_required
def visualizar_grupos_flashcard(request):
    if request.method == 'GET':

        grupos_flashcard = GrupoFlashcard.objects.all()

        context = {
            'grupos_flashcard': grupos_flashcard
        }

        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_grupos.html',
            context
        )
@login_required
def visualizar_grupo_flashcard(request, tema):
    if request.method == 'GET':
        grupo_flashcard = get_object_or_404(GrupoFlashcard, tema=tema)

        context = {
            'grupo_flashcard': grupo_flashcard
        }

        return render(
            request,
            'flashcard/grupos_flashcard/visualizar_um_grupo.html',
            context
        )
@login_required
def excluir_grupo_flashcard(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/grupos_flashcard/excluir_grupo.html'
        )
@login_required
def editar_grupo_flashcard(request, tema):
    if request.method == 'GET':
        grupo_flashcard = get_object_or_404(GrupoFlashcard, tema=tema)
        form = GrupoFlashcardForm(instance=grupo_flashcard)

        context = {
            'form': form
        }

        return render(
            request,
            'flashcard/grupos_flashcard/editar_grupo.html',
            context
        )

@login_required
def escolher_grupo_flashcard(request, proxima_pagina):
    if request.method == 'GET':
        grupos_flashcard = GrupoFlashcard.objects.all()

        context = {
            'grupos_flashcard': grupos_flashcard,
            'proxima_pagina': proxima_pagina
        }

        return render(
            request,
            'flashcard/escolher_grupo.html',
            context
        )

@login_required
def revisao(request):
    if request.method == 'GET':
        return render(
            request,
            'flashcard/revisao/pratica.html'
        )