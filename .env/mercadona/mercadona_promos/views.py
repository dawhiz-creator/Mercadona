from django.shortcuts import render
from .models import Categorie, Produit, Promotion


def catalogue(request):
    """
    Vue permettant d'afficher le catalogue des produits avec les promotions en cours.

    :param request: la requête HTTP reçue par la vue
    :return: la réponse HTTP contenant la page HTML du catalogue
    """
    promotions = Promotion.objects.all().order_by('pourcentage')
    categories = Categorie.objects.all()
    produits = Produit.objects.all()

    categorie = request.GET.get('categorie')
    if categorie:
        produits = Produit.objects.filter(categorie__libelle=categorie)

    return render(request, 'catalogue.html', {'categories': categories,
                                              'produits': produits,
                                              'promotions': promotions})

def mentions(request):
    """
    Renvoie la page de mentions légales du site web.
    """
    return render(request, 'mentions.html')

def confidentialites(request):
    """
    Renvoie la page de politique de confidentialité du site web.
    """
    return render(request, 'confidentialites.html')

def conditions(request):
    """
    Renvoie la page de conditions générales d'utilisation du site web.
    """
    return render(request, 'conditions.html')
