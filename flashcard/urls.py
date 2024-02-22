from django.urls import path

from flashcard import views

app_name = 'flashcard'

urlpatterns = [
    # Página inicial
    path('', views.HomeView.as_view(), name='home'),

    # Usuário
    path('usuario/login/', views.Login.as_view(), name='login'),
    path('usuario/cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('usuario/logout/', views.Logout.as_view(), name='logout'),

    # Flashcards
    path('flashcard/criacao/tipo/<str:tema_grupo>', views.tipo_criacao_flashcard, name='tipo_criacao_flashcard'),
    path('flashcard/criar/<str:tipo_flashcard>/<str:grupo_flashcard>/', views.criar_flashcard, name='criar_flashcard'),
    path('flashcard/visualizar/<str:palavra_frente>/', views.visualizar_flashcard, name='visualizar_flashcard'),
    path('flashcard/editar/', views.editar_flashcard, name='editar_flashcard'),
    path('flashcard/excluir/', views.excluir_flashcard, name='excluir_flashcard'),

    # Grupos flashcard
    path('flashcard/grupos/', views.visualizar_grupos_flashcard, name='visualizar_grupos'),
    path('flashcard/grupo/criar/', views.criar_grupo_flashcard, name='criar_grupo_flashcard'),
    path('flashcard/grupo/visualizar/<str:tema>/', views.visualizar_grupo_flashcard, name='visualizar_grupo_flashcard'),
    path('flashcard/grupo/editar/<str:tema>/', views.editar_grupo_flashcard, name='editar_grupo_flashcard'),
    path('flashcard/grupo/excluir/', views.excluir_grupo_flashcard, name='excluir_grupo_flashcard'),
    path('flashcard/grupo/selecionar/<str:proxima_pagina>/', views.escolher_grupo_flashcard, name='escolher_grupo_flashcard'),
    path('flashcard/grupo/revisao/', views.revisao, name='revisao'),
]
