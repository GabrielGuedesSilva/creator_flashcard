from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from flashcard.models import Flashcard


class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class FlashcardForm (forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = [
            'palavra_frente',
            'imagem',
        ]

        labels = {
            'palavra_frente': 'Palavra a ser Memorizada'
        }

