# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle


class Promotion(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.produit.libelle
