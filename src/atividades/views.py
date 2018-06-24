from django.shortcuts import render, redirect, get_object_or_404
from .models import Atividade
from .forms import AtividadeForm


def listar_atividades(request):
    """[View responsável por direcionar a requisição do usuário
    para a página de listagem de atividades já criadas]

    Args:
        [request] ([HttpRequest]): [Objeto de requesição  do usuário criada pelo FrameWork]

    Returns:
        [render]: [Função auxiliar do framework, que gera um template seguido de um contexto a ser utilziado pelo template]
    """
    atividades = Atividade.object.all();
    return render(request, 'pages/atividades.html', {'atividades': atividades.order_by('nome')})


def criar_atividade(request):
    """[View resposável  por sintetizar um formulário de cadastro de atividades em uma página HTML 
      ou gravar no BD os dados gerados pelo POST da requisição]

    Args:
        request ([HttpRequest]): [Objeto que contem metadados sobre a requisição]

    Returns:
        [HttpResponse]: [Combina um template e um contexto e retorna um objeto HttpResponse com o texto renderizado]
    """
    form_atividade = AtividadeForm(request.POST or None)


    if(form_atividade.is_valid()):
        form_atividade.save()
        return redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})


def editar_atividade(request, id):

    """[View resposável por sintetizar um formulário de edição de atividades em uma página HTML 
     ou gravar no BD os dados alterados pelo POST da requisição]

    Args:
        request([HttpRequest]): [Objeto que contem metadados sobre a requisição]
        id([int]): [Número de índice primário utilizado para obter um objeto Atividade no banco de dados]

    Returns:
        [HttpResponse]: [Combina um template e um contexto e retorna um objeto HttpResponse com o texto renderizado]
    """
    atividade = get_object_or_404(Atividade, pk=id)
    form_atividade = AtividadeForm(request.POST or None, instance=atividade)

    if(form_atividade.is_valid()):
        form_atividade.save()
        return redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})


def deletar_atividade(request, id):
    """[View resposável por sintetizar um formulário de deleção de atividades em uma página HTML  
    ou gravar no BD os dados removidos pelo POST da requisição]

    Args:
        request([HttpRequest]): [Objeto que contem metadados sobre a requisição]
        id([int]): [Número de índice primário utilizado para obter um objeto Atividade no banco de dados]

    Returns:
        [HttpResponse]: [Combina um template e um contexto e retorna um objeto HttpResponse com o texto renderizado]
    """
    atividade = get_object_or_404(Atividade, pk=id)
    form_atividade = AtividadeForm(request.POST or None, instance=atividade)

    if request.method == 'POST':
        atividade.delete()
        return redirect('playlist')

    return render(request, 'pages/atividade_delete_confirm.html', {'form': form_atividade})
