"""bestiario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bestiario_frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexRedirect, name='index'),
    path('login/', views.loginBestiario, name='login'),
    path('cadastro/', views.registrarUsuario, name='cadastro'),
    path('painel/', views.painel, name='painel'),
    path('cadastrar-criatura/', views.criarCriatura, name='cadastrar-criatura'),
    path('criaturas-cadastradas/', views.criaturasCadastradas, name='criaturas-cadastradas'),
    path('criaturas-cadastradas/<id>/', views.detalhesCriaturas, name='detalhes-criatura'),
    path('cadastrar-monstro/', views.criarMonstro, name='cadastrar-monstro'),
    path('monstros-cadastrados/', views.monstrosCadastrados, name='monstros-cadastrados'),
    path('monstros-cadastrados/<id>/', views.detalhesMonstros, name='detalhes-monstro'),
    path('cadastrar-personagem/', views.criarPersonagem, name='cadastrar-personagem'),
    path('personagens-cadastrados/', views.personagensCadastrados, name='personagens-cadastrados'),
    path('personagens-cadastrados/<id>/', views.detalhesPersonagens, name='detalhes-personagens'),
    path('editar-criatura/<id>/', views.editarCriatura, name='editar-criatura'),
    path('remover-criatura/<id>', views.removerCriatura, name='remover-criatura'),
    path('editar-monstro/<id>/', views.editarMonstro, name='editar-monstro'),
    path('remover-monstro/<id>', views.removerMonstro, name='remover-monstro'),
    path('logout/', views.logoutUsuario, name='logout'),
]
