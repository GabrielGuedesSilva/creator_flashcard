from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from fake_dados import fake
from flashcard.forms import FlashcardForm, FlashcardSimplesForm
from flashcard.models import Flashcard, GrupoFlashcard

from reverso_context_api import Client

@login_required()
def tipo_criacao_flashcard(request, tema_grupo):
    if request.method == 'GET':

        context = {
            'tema_grupo': tema_grupo
        }

        return render(
            request,
            'flashcard/tipo_criacao_flashcard.html',
            context
        )


@login_required
def visualizar_flashcard(request, palavra_frente):
    if request.method == 'GET':

        flashcard = Flashcard.objects.filter(palavra_frente=palavra_frente).first()

        context = {
            'flashcard': flashcard
        }

        return render(
            request,
            'flashcard/visualizar_flashcard.html',
            context
        )


def gera_opcoes(palavra_frente):
    opcoes = []
    opcoes.append(palavra_frente)

    for i in range(3):
        palavra_aleatoria = fake.word()

        while palavra_aleatoria in opcoes:
            palavra_aleatoria = fake.word()

        opcoes.append(palavra_aleatoria)

    return opcoes




@login_required
def criar_flashcard(request, tipo_flashcard, grupo_flashcard):
    if request.method == 'GET':

        if tipo_flashcard == 'personalizado':
            form = FlashcardForm()
        else:
            form = FlashcardSimplesForm()

        context = {
            'form': form,
            'tipo_flashcard': tipo_flashcard,
            'grupo_flashcard': grupo_flashcard
        }

        return render(
            request,
            'flashcard/criar_flashcard.html',
            context
        )

    if request.method == 'POST':
        if tipo_flashcard == 'personalizado':
            form = FlashcardForm(request.POST)

            if form.is_valid():
                flashcard = Flashcard(**form.cleaned_data)
                flashcard.usuario_pertencente = request.user
                flashcard.grupo_pertencente = GrupoFlashcard.objects.get(tema=grupo_flashcard)
                flashcard.opcoes_revisao = gera_opcoes(flashcard.palavra_frente)
                flashcard.save()

            return redirect('flashcard:visualizar_flashcard', palavra_frente=flashcard.palavra_frente)
        else:
            form = FlashcardSimplesForm(request.POST)

            if form.is_valid():
                flashcard = Flashcard(**form.cleaned_data)
                flashcard.usuario_pertencente = request.user
                flashcard.grupo_pertencente = GrupoFlashcard.objects.get(tema=grupo_flashcard)

                client = Client("en", "pt")

                traducao_verso = list(client.get_translations("love"))[0]
                flashcard.traducao_verso = traducao_verso

                frases_aplicacao = next(client.get_translation_samples("love", cleanup=True))
                flashcard.frase_aplicacao_verso_original = frases_aplicacao[0]
                flashcard.frase_aplicacao_verso_traduzida = frases_aplicacao[1]
                flashcard.opcoes_revisao = gera_opcoes(flashcard.palavra_frente)
                flashcard.save()

                return redirect('flashcard:visualizar_flashcard', palavra_frente=flashcard.palavra_frente)



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
