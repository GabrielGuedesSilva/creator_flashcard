from django.contrib import admin

from flashcard import models


@admin.register(models.GrupoFlashcard)
class GrupoFlashcardAdmin(admin.ModelAdmin):
    list_display = ['id', 'tema', 'descricao', 'usuario_pertencente']
    ordering = ('-id',)
    list_display_links = ['tema']
    search_fields = ['tema', 'usuario_pertencente__username']
@admin.register(models.Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['id', 'palavra_frente', 'traducao_verso', 'frase_aplicacao_verso_original']
    ordering = ('-id',)
    list_display_links = ['palavra_frente']
    search_fields = ['palavra_frente', 'traducao_verso', 'grupo_pertencente__tema']

