from django.urls import path
from .views import listar_atividades, criar_atividade, editar_atividade

urlpatterns= [
    path('playlist/', listar_atividades, name = 'playlist'),
    path('criar/', criar_atividade, name= 'criar_atividade'),
    path('editar/<int:id>/', editar_atividade, name = 'editar_atividade')
]