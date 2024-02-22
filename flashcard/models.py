from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class GrupoFlashcard(models.Model):
    usuario_pertencente = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.tema}'

class Flashcard(models.Model):
    grupo_pertencente = models.ForeignKey(GrupoFlashcard, on_delete=models.CASCADE, related_name='flashcards')
    usuario_pertencente = models.ForeignKey(User, on_delete=models.CASCADE)
    palavra_frente = models.CharField(max_length=255)
    traducao_verso = models.CharField(max_length=255, default='')
    frase_aplicacao_verso_original = models.TextField(blank=True, null=True)
    frase_aplicacao_verso_traduzida = models.TextField(blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True)
    info_adicional = models.TextField(blank=True, null=True, default='Sem informações adicionais')
    opcoes_revisao = ArrayField(models.CharField(max_length=255), size=4, null=True, default=list)
    girar_flashcard = models.BooleanField(default=True)

class Revisao (models.Model):
    grupo_flashcard = models.ForeignKey(GrupoFlashcard, on_delete=models.CASCADE)
    quantidade_flashcards_revisados = models.IntegerField()
    quantidade_acertos = models.IntegerField()
    quantidade_erros = models.IntegerField()
