from django.urls import path
from .views import listar_atividades

urlpatterns= [
    path('playlist', listar_atividades, name = 'playlist'),
]