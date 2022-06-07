from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(unique=True, max_length=100)
    campanha = models.CharField(max_length=256)
    email = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'usuario'

class Criatura(models.Model):
    nickname = models.CharField(unique=True, max_length=100)
    atributos = models.TextField()
    status_combate = models.CharField(max_length=1024)
    tamanho = models.CharField(max_length=1024)
    conhecimento = models.CharField(max_length=1024)
    alinhamento = models.CharField(max_length=1024)
    resistencia = models.CharField(max_length=1024)
    acoes = models.TextField()
    magias = models.TextField()

    class Meta:
        db_table = 'criatura'

class Monstro(models.Model):
    nickname = models.ForeignKey(Criatura, on_delete=models.CASCADE)
    imagem_url = models.TextField(max_length=2048)
    tipo = models.CharField(max_length=256)
    nivel_dificuldade = models.CharField(max_length=256)
    vida_max = models.IntegerField()
    vida_min = models.IntegerField()

    class Meta:
        db_table = 'monstro'

class Personagem(models.Model):
    nickname = models.ForeignKey(Criatura, on_delete=models.CASCADE)
    nome = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=1024)
    armas = models.TextField()
    talento = models.CharField(max_length=1024)
    mochila = models.TextField()
    classe = models.CharField(max_length=1024)

    class Meta:
        db_table = 'personagem'