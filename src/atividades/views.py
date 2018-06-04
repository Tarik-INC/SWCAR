from django.shortcuts import render, redirect, get_object_or_404
from .models import Atividade
from .forms import AtividadeForm

def listar_atividades(request):
    atividades = Atividade.object.all();
    return render(request, 'pages/atividades.html', {'atividades':atividades.order_by('nome')})


def criar_atividade(request):
    form_atividade = AtividadeForm(request.POST or None)
    
    if(form_atividade.is_valid()):
        form_atividade.save()
        return  redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})


def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, pk = id)
    form_atividade = AtividadeForm(request.POST or None, instance = atividade)

    if(form_atividade.is_valid()):
        form_atividade.save()
        return redirect('playlist')

    return render(request, 'pages/atividade_form.html', {'form': form_atividade})