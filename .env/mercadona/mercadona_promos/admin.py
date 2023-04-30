
# Register your models here.
# from django.contrib import admin
from .models import Categorie
from django.contrib import admin
from .models import Categorie, Produit, Admin, Promotion


class CategorieAdmin(admin.ModelAdmin):
    # champ à afficher dans la liste des catégories
    list_display = ('libelle',)
    search_fields = ('libelle',)  # champ utilisé pour la recherche
    ordering = ('libelle',)  # ordre de tri par défaut


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'prix', 'categorie', 'description', 'image')
    search_fields = ('libelle', 'categorie__libelle',)
    list_filter = ('categorie',)
    ordering = ('libelle',)


# class AdminAdmin(admin.ModelAdmin):
#     list_display = ('email', 'nom', 'prenom',)
#     search_fields = ('email', 'nom', 'prenom',)
#     ordering = ('nom',)

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('produit', 'date_debut', 'date_fin', 'pourcentage',)
    search_fields = ('produit__libelle',)
    ordering = ('date_debut',)


class AdminAdmin(admin.ModelAdmin):  # Modification du nom de la classe
    list_display = ('nom', 'mot_de_passe',)  # Ajout du champ mot_de_passe
    # Modification des champs utilisés pour la recherche
    search_fields = ('nom',)
    ordering = ('nom',)


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Promotion, PromotionAdmin)
