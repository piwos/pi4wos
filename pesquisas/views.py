import csv
import io

import pandas as pd
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PesquisaForm
from .models import Pesquisa


def save_data(data):
    aux = []
    for item in data:
        autores = item.get('Autores')
        titulo = item.get('Título')
        fonte_artigo = item.get('Fonte do artigo')
        palavras_chave = item.get('Palavras-chave')
        resumo_artigo = item.get('Resumo do artigo')
        endereco_autores = item.get('Endereço dos Autores')
        instituicao_autores = item.get('Instituição de vínculo dos autores')
        agencia_fomento = item.get('Agência de Fomento')
        contagem_citacoes = item.get('Contagem do número de citações')
        ano_publicacao = item.get('Ano da publicação')
        areas_pesquisa = item.get('Áreas de pesquisa')
        obj = Pesquisa(
            autores = autores,
            titulo = titulo,
            fonte_artigo = fonte_artigo,
            palavras_chave = palavras_chave,
            resumo_artigo = resumo_artigo,
            endereco_autores = endereco_autores,
            instituicao_autores = instituicao_autores,
            agencia_fomento = agencia_fomento,
            contagem_citacoes = contagem_citacoes,
            ano_publicacao = ano_publicacao,
            areas_pesquisa = areas_pesquisa,            
        )
        aux.append(obj)
    Pesquisa.objects.bulk_create(aux)


def pesquisas_home(request):
    return render(request, 'pesquisas.html')


def pesquisas_cadastrar(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]        
        save_data(data)
        return HttpResponseRedirect(reverse('pesquisas_home'))
    return render(request, 'cadastrar.html')


def pesquisas_listar(request):
    pesquisas_list = Pesquisa.objects.all()
    paginator = Paginator(pesquisas_list, 5)

    page = request.GET.get('page')

    try:
        pesquisas = paginator.page(page)
    except PageNotAnInteger:
        pesquisas = paginator.page(1)
    except EmptyPage:
        pesquisas = paginator.page(paginator.num_pages)
    
    return render(request, 'listar.html', {'pesquisas': pesquisas})


def pesquisas_editar(request, id):
    context = {}
    pesquisa = get_object_or_404(Pesquisa, pk=id)
        
    if(request.method == 'POST'):
        form = PesquisaForm(request.POST, instance=pesquisa)
        if form.is_valid():
            form.save()
        return redirect('pesquisas_listar')
    form = PesquisaForm(instance=pesquisa)    
    return render(request, 'editar.html', {'form': form})


def pesquisas_deletar(request, id):
    pesquisa = Pesquisa.objects.get(id=id)
    pesquisa.delete()
    pesquisas = Pesquisa.objects.all()
    return render(request, 'listar.html', {'pesquisas': pesquisas})


def pesquisas_pesquisar(request):
    query = request.GET.get('query')
    resultados = Pesquisa.objects.filter(instituicao_autores__icontains=query)
    return render(request, 'resultado.html', {'resultados': resultados, 'termo': query},)


def pesquisas_grafico(request):
    pesquisas = Pesquisa.objects.values('instituicao_autores')
    df_counts = pd.DataFrame(pesquisas)
    df_counts = df_counts.value_counts(dropna=False).reset_index()
    df_counts.columns = ['Instituição', 'Citação']    
    df10 = df_counts.iloc[:10]
    dfl = df10.values.tolist()    
    for i in range(len(dfl)):
        for j in range(len(dfl[i])):
            if dfl[i][j] == '':
                dfl[i][j] = 'Instituição não definida'
    return render(request,'grafico.html', {'dflist': dfl})
