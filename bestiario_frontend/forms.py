from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Usuario, Criatura, Monstro, Personagem

class loginForm(AuthenticationForm):
    pass

class RegisterUsuarioForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ['nome', 'password', 'campanha', 'email']

class RegisterCriaturaForm(ModelForm):
    class Meta:
        model = Criatura
        fields = [
            'nickname',
            'acoes',
            'resistencia',
            'magias',
            'status_combate',
            'alinhamento',
            'tamanho',
            'conhecimento',
            'atributos',
            ]

class RegisterMonstroForm(ModelForm):
    class Meta:
        model = Monstro
        fields = [
            'nickname',
            'imagem_url',
            'tipo',
            'nivel_dificuldade',
            'vida_max',
            'vida_min',
            ]

class RegisterPersonagemForm(ModelForm):
    class Meta:
        model = Personagem
        fields = [
            'nickname',
            'nome',
            'nivel',
            'armas',
            'talento',
            'mochila',
            'classe',
            ]