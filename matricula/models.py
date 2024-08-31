from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    curso = models.CharField(max_length=30)