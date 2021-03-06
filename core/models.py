from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class Livro(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=50)
    editora = models.ForeignKey('Editora')

    def __str__(self):
        return self.titulo

class Editora(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
