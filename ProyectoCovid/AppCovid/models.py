from django.db import models

# Create your models here.
class Guantes(models.Model):
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()
    esPremium = models.BooleanField(null=True)

    def __str__(self):

        return f"GUANTES: {self.marca} Tamaño: {self.tamanio} Precio: {self.precio} Es Premium: {self.esPremium} "

class Barbijos(models.Model):
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()

class Oximetros(models.Model):
    marca= models.CharField(max_length=40)
    origen= models.CharField(max_length=40)
    precio= models.IntegerField()
    esImportado= models.BooleanField(null=True)
