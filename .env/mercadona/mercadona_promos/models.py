# Create your models here.
from typing import Optional
from io import BytesIO
import bcrypt

from django.db import models
from django.core.files import File
from django.core.files.base import ContentFile
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch
from babel.dates import format_date
import requests


class Categorie(models.Model):
    """Modèle représentant une catégorie de produits."""
    libelle = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.libelle


class Promotion(models.Model):
    """Modèle représentant une promotion sur un produit."""
    date_debut = models.DateField()
    date_fin = models.DateField()
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, related_name='promotions')

    def __str__(self) -> str:
        return self.produit.libelle

    def date_debut_promo(self) -> str:
        """
        Retourne la date de début de la promotion formatée en chaîne de
        caractères selon le format "d MMMM y".
        """
        return format_date(self.date_debut, format='d MMMM y', locale='fr')

    def date_fin_promo(self) -> str:
        """
        Retourne la date de fin de la promotion formatée en chaîne de
        caractères selon le format "d MMMM y".
        """
        return format_date(self.date_fin, format='d MMMM y', locale='fr')


class Produit(models.Model):
    """Modèle représentant un produit."""
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(max_length=300)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, null=True,
        blank=True, related_name='produits_with_promo')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.libelle

    def prix_avant_promo(self) -> float:
        """Retourne le prix du produit avant application de la promotion."""
        return self.prix
       
    def prix_apres_promo(self) -> Optional[float]:
        """Retourne le prix du produit après application de la promotion."""
        if self.promotion:
            prix_promo = self.prix - (self.prix *
                                      self.promotion.pourcentage / 100)
            return round(prix_promo, 2)
        else:
            return round(self.prix, 2)

    @property
    def image(self) -> Optional[File]:
        """Retourne l'image du produit."""
        if self.image_url:
            response = requests.get(self.image_url)
            fp = BytesIO()
            fp.write(response.content)
            return File(fp)
        else:
            return None


class Admin(models.Model):
    """Modèle représentant un administrateur."""
    nom = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)

    class Meta:
        """
        Métadonnées pour le modèle Admin.
        """
        verbose_name = _("admin")
        verbose_name_plural = _("admins")

    def save(self, *args, **kwargs) -> None:
        if not self.pk:  # only hash password if creating a new object
            self.mot_de_passe = bcrypt.hashpw(
                self.mot_de_passe.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nom