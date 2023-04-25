

# # Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# from django.utils import timezone
# from .models import Produit, Categorie, Promotion
# from .forms import ProduitForm, PromotionForm


# def catalogue(request):
#     produits = Produit.objects.all()

#     categorie_param = request.GET.get('categorie')
#     if categorie_param:
#         produits = produits.filter(categorie__libelle=categorie_param)

#     context = {
#         'produits': produits,
#         'categories': Categorie.objects.all()
#     }
#     return render(request, 'catalogue.html', context)
#     # return render(request, 'catalogue.html', context)


# @login_required
# @staff_member_required
# def ajouter_produit(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST, request.FILES)
#         if form.is_valid():
#             produit = form.save(commit=False)
#             produit.pub_date = timezone.now()
#             produit.save()
#             return redirect('catalogue')
#     else:
#         form = ProduitForm()
#     return render(request, 'ajouter_produit.html', {'form': form})


# @login_required
# @staff_member_required
# def ajouter_promotion(request, produit_id):
#     produit = Produit.objects.get(pk=produit_id)

#     if request.method == 'POST':
#         form = PromotionForm(request.POST)
#         if form.is_valid():
#             promotion = form.save(commit=False)
#             promotion.produit = produit
#             promotion.save()
#             return redirect('catalogue')
#     else:
#         form = PromotionForm()
#     return render(request, 'ajouter_promotion.html', {'form': form, 'produit': produit})

from django.shortcuts import render
from .models import Categorie, Produit


def catalogue(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.all()

    categorie = request.GET.get('categorie')
    if categorie:
        produits = Produit.objects.filter(categorie__libelle=categorie)

    return render(request, 'catalogue.html', {'categories': categories, 'produits': produits})
