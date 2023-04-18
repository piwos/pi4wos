from django.contrib import admin

from .models import Pesquisa


# admin.site.register(Post)
@admin.register(Pesquisa) # decorador registra a classe ModelAdmin
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('autores', 'titulo', 'instituicao_autores', 'agencia_fomento')
    list_filter = ('autores', 'titulo', 'instituicao_autores', 'agencia_fomento')
    search_fields = ('autores', 'titulo', 'instituicao_autores', 'agencia_fomento')
    ordering = ('autores',)
    readonly_fields = ['registro_criado', 'registro_atualizado']
