<<<<<<< HEAD
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
=======
# # # Create your models here.
# # from django.db import models
# # from django.contrib.auth.models import User


# # class Categorie(models.Model):
# #     libelle = models.CharField(max_length=100)
>>>>>>> 66eafce (Revert "ADD promo display logic + corresponding DB sets")

# #     def __str__(self):
# #         return self.libelle

<<<<<<< HEAD
=======

# # class Produit(models.Model):
# #     libelle = models.CharField(max_length=100)
# #     description = models.TextField()
# #     prix = models.DecimalField(max_digits=10, decimal_places=2)
# #     image = models.ImageField(upload_to='images/')
# #     categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.libelle


# # class Promotion(models.Model):
# #     debut = models.DateField()
# #     fin = models.DateField()
# #     pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
# #     produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.produit.libelle

from django.db import models
import bcrypt

class Categorie(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle
>>>>>>> 66eafce (Revert "ADD promo display logic + corresponding DB sets")

class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField()
<<<<<<< HEAD
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
=======
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='produits/')
>>>>>>> 66eafce (Revert "ADD promo display logic + corresponding DB sets")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

<<<<<<< HEAD
=======

    def prix_apres_promo(self):
        if self.promotion:
            prix_promo = self.prix - (self.prix * self.promotion.pourcentage / 100)
            return "{:.2f}".format(prix_promo)
        else:
            return "{:.2f}".format(self.prix)
>>>>>>> 66eafce (Revert "ADD promo display logic + corresponding DB sets")

class Promotion(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.produit.libelle
