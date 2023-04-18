from django import forms

from .models import Pesquisa


class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        # fields = '__all__'
        fields = ['autores', 
                'titulo', 
                'fonte_artigo', 
                'palavras_chave', 
                'resumo_artigo', 
                'endereco_autores', 
                'instituicao_autores', 
                'agencia_fomento', 
                'contagem_citacoes', 
                'ano_publicacao', 
                'areas_pesquisa',
        ]
