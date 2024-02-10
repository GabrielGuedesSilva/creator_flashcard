from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

class GrupoFlashcards(models.Model):
    usuario_pertencente = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    descricao = models.TextField()

class Flashcard(models.Model):
    grupo_pertencente = models.ForeignKey(GrupoFlashcards, on_delete=models.CASCADE)
    usuario_pertencente = models.ForeignKey(User, on_delete=models.CASCADE)
    palavra_frente = models.CharField(max_length=255)
    traducao_verso = models.CharField(max_length=255)
    frase_aplicacao_verso = models.TextField()
    imagem = models.ImageField()
    info_adicional = models.TextField()
    opcoes_revisao = ArrayField(models.CharField(max_length=255), size=4)
    girar_flashcard = models.BooleanField(default=True)

class Revisao (models.Model):
    grupo_flashcard = models.ForeignKey(GrupoFlashcards, on_delete=models.CASCADE)
    quantidade_flashcards_revisados = models.IntegerField()
    quantidade_acertos = models.IntegerField()
    quantidade_erros = models.IntegerField()
