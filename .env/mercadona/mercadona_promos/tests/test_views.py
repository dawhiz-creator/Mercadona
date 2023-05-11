from django.test import Client, TestCase
from django.urls import reverse
from mercadona_promos.models import Produit, Categorie

'''
Vérifier que la page de promotion affiche un message approprié lorsqu'il n'y a 
pas de produit en promotion.
'''

class PromotionPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_promotion(self):
        response = self.client.get(reverse('promotion'))
        self.assertContains(response, "Aucun produit en promotion pour le moment.")

'''
Vérifier que la page de promotion affiche les produits en promotion.
'''
class PromotionPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produit = Produit.objects.create(libelle='test', prix=10, categorie='Vetements')
        self.promotion = Promotion.objects.create(produit=self.produit, reduction=0.2)

    def test_promotion_list(self):
        response = self.client.get(reverse('promotion'))
        self.assertContains(response, self.produit.libelle)
        self.assertContains(response, self.produit.categorie)
        self.assertContains(response, self.produit.prix)
        self.assertContains(response, self.produit.prix_apres_promo)

'''
Vérifier que les filtres de catégorie fonctionnent correctement.
'''
class PromotionPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produit1 = Produit.objects.create(libelle='test1', prix=10, categorie='Vetements')
        self.produit2 = Produit.objects.create(libelle='test2', prix=20, categorie='Electronique')
        self.categorie1 = Categorie.objects.create(libelle='Vetements')
        self.categorie2 = Categorie.objects.create(libelle='Electronique')
        self.produit1.categories.add(self.categorie1)
        self.produit2.categories.add(self.categorie2)

    def test_categorie_filter(self):
        response = self.client.get(reverse('promotion') + '?categorie=Vetements')
        self.assertContains(response, self.produit1.libelle)
        self.assertNotContains(response, self.produit2.libelle)

        response = self.client.get(reverse('promotion') + '?categorie=Electronique')
        self.assertContains(response, self.produit2.libelle)
        self.assertNotContains(response, self.produit1.libelle)

'''
Vérifier que les icônes de catégorie sont correctement affichées.
'''
class PromotionPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.produit1 = Produit.objects.create(libelle="Produit 1", description="Description produit 1", prix=10.0)
        self.produit2 = Produit.objects.create(libelle="Produit 2", description="Description produit 2", prix=20.0)
        self.categorie = Categorie.objects.create(nom="categorie test")
        self.produit1.categories.add(self.categorie)
        self.produit2.categories.add(self.categorie)