from django.shortcuts import render
from .models import Atividade

def listar_atividades(request):
    atividades = Atividade.object.all();
    return render(request, 'pages/atividades.html', {'atividades':atividades})
