from django.shortcuts import render, get_object_or_404
from .models import Categorie, Produit, Promotion

#Catalog_page
from datetime import date

def catalogue(request):
    promotions = Promotion.objects.all().order_by('pourcentage')
    categories = Categorie.objects.all()
    produits = Produit.objects.all()

    categorie = request.GET.get('categorie')
    if categorie:
        produits = Produit.objects.filter(categorie__libelle=categorie)

    return render(request, 'catalogue.html', {'categories': categories, 'produits': produits, 'promotions': promotions})

def mentions(request):
    return render(request, 'mentions.html')

def confidentialites(request):
    return render(request, 'confidentialites.html')

def conditions(request):
    return render(request, 'conditions.html')