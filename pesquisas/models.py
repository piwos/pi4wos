from django.contrib.auth.models import User
from django.db import models


class Pesquisa(models.Model):
    autores = models.TextField('Autor', null=True, blank=True)
    titulo = models.TextField('Título', null=True, blank=True)
    fonte_artigo = models.TextField('Fonte', null=True, blank=True)
    palavras_chave = models.TextField('Palavra chave', null=True, blank=True)
    resumo_artigo = models.TextField('Resumo', null=True, blank=True)
    endereco_autores = models.TextField('Endereço', null=True, blank=True)
    instituicao_autores = models.TextField('Instituição', null=True, blank=True)
    agencia_fomento = models.TextField('Agência', null=True, blank=True)
    contagem_citacoes = models.PositiveIntegerField('Citação', default=1)
    ano_publicacao = models.CharField('Publicação', max_length=10, null=True, blank=True)
    areas_pesquisa = models.CharField('Área pesquisa', max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    registro_criado = models.DateTimeField(auto_now_add=True)
    registro_atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pesquisa'
        verbose_name_plural = 'Pesquisas'
        ordering = ['id']
    
    def __str__(self):
        return self.titulo
