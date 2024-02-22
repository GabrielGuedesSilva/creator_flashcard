from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from flashcard.models import Flashcard, GrupoFlashcard


class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class GrupoFlashcardForm(forms.ModelForm):
     class Meta:
         model = GrupoFlashcard
         fields = [
             'tema',
             'descricao',
         ]

         labels = {
             'tema': 'Tema',
             'descricao': 'Descrição'
         }

class FlashcardForm (forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = [
            'palavra_frente',
            'traducao_verso',
            'frase_aplicacao_verso_original',
            'frase_aplicacao_verso_traduzida',
            'imagem',
            'info_adicional'
        ]

        labels = {
            'palavra_frente': 'Palavra a ser Memorizada',
            'traducao_verso': 'Tradução',
            'frase_aplicacao_verso_original': 'Frase de aplicação',
            'frase_aplicacao_verso_traduzida': 'Frase de aplicação Traduzida',
            'info_adicional': 'Informações adicionais'
        }

class FlashcardSimplesForm (forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = [
            'palavra_frente',
        ]

        labels = {
            'palavra_frente': 'Palavra a ser Memorizada'
        }
