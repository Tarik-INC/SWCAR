from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import listar_atividades, criar_atividade, editar_atividade, deletar_atividade, cadastrar_usuario, inicio, selecionar_atividade

urlpatterns = [
    path('playlist/', listar_atividades, name='playlist'),
    path('criar/', criar_atividade, name='criar_atividade'),
    path('editar/<int:id>/', editar_atividade, name='editar_atividade'),
    path('deletar/<int:id>/', deletar_atividade, name='deletar_atividade'),
    path('cadastrar_usuario/', cadastrar_usuario, name = 'cadastrar_usuario' ),
    path('inicio/', inicio, name = 'inicio'),
    path('atividade/<str:nome>/', selecionar_atividade, name = 'atividade_selecionada')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
