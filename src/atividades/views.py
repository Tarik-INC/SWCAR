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
    return render(request, 'pages/atividades.html', {'atividades':atividades.order_by('nome')})


def criar_atividade(request):
    """[View responsável por direcionar a requisição do usuário
     para a página de criação de atividade]
    
    Args:
        [request] ([HttpRequest]): [Objeto de requesição  do usuário criada pelo FrameWork]
    
    Returns:
        [render]: [Função auxiliar do framework, que gera um template seguido de um contexto a ser utilziado pelo template]
    """
    form_atividade = AtividadeForm(request.POST or None)
    
    if(form_atividade.is_valid()):
        form_atividade.save()
        return  redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})


def editar_atividade(request, id):
    """[View responśavel por direcionar a requisição do usuário
     para a página de criação de ativida]
    
    Args:
        [request] ([HttpRequest]): [Objeto de requesição  do usuário criada pelo FrameWork]
    
    Returns:
        [render]: [Função auxiliar do framework, que gera um template seguido de um contexto a ser utilziado pelo template]
    """

    atividade = get_object_or_404(Atividade, pk = id)
    form_atividade = AtividadeForm(request.POST or None, instance = atividade)

    if(form_atividade.is_valid()):
        form_atividade.save()
        return redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})