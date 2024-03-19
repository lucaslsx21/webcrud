from django.db import models

# Create your models here.
class Person(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=254)