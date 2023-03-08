from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.pesquisas_home, name='pesquisas_home'),
    path('cadastrar/', views.pesquisas_cadastrar, name='pesquisas_cadastrar'),
    path('listar/', views.pesquisas_listar, name='pesquisas_listar'),
    path('pesquisar/', views.pesquisas_pesquisar, name='pesquisas_pesquisar'),
    path('editar/<int:id>', views.pesquisas_editar, name='pesquisas_editar'),
    path('<int:id>', views.pesquisas_deletar, name='pesquisas_deletar'),
    path('grafico/', views.pesquisas_grafico, name='pesquisas_grafico'),
]