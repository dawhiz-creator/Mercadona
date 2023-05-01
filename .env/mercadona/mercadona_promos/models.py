# # # Create your models here.
from django.db import models
import bcrypt
from babel.dates import format_date

class Categorie(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

class Promotion(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, related_name='promotions')

    def __str__(self):
        return self.produit.libelle

    # retour dates au format français

    def date_debut_promo(self):
        return format_date(self.date_debut, format='d MMMM y', locale='fr')

    def date_fin_promo(self):
        return format_date(self.date_fin, format='d MMMM y', locale='fr')

class Produit(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='produits/')
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, null=True, blank=True, related_name='produits_with_promo')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

    def prix_avant_promo(self):
        return self.prix

    def prix_apres_promo(self):
        if self.promotion:
            prix_promo = self.prix - (self.prix * self.promotion.pourcentage / 100)
            return "{:.2f}".format(prix_promo)
        else:
            return "{:.2f}".format(self.prix)

class Admin(models.Model):
    nom = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:  # only hash password if creating a new object
            self.mot_de_passe = bcrypt.hashpw(self.mot_de_passe.encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom