from django.urls import path
from . import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home'),
]

#Imagem
urlpatterns += [
    path('imagem/', views.listaImagem.as_view(), name='Imagem'),
    path('imagem/add', views.cadastroImagem, name='ImagemCadastro'),
    path('imagem/<int:pk>', views.detalhesImagem.as_view(), name='ImagemDetalhes'),
    path('imagem/delete<int:pk>', views.excluirImagem, name='ImagemExcluir'),
]