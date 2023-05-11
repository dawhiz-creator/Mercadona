'''
création d'objets Categorie, Promotion, Produit et Admin pour s'assurer 
qu'ils sont correctement stockés dans la base de données
'''

from datetime import date
from django.test import TestCase
from mercadona_promos.models import Categorie, Promotion, Produit, Admin

class ModelTests(TestCase):
    def test_create_categorie(self):
        c = Categorie.objects.create(libelle="Fruits")
        self.assertEqual(c.libelle, "Fruits")
        
    def test_create_promotion(self):
        c = Categorie.objects.create(libelle="Légumes")
        p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", promotion=None, categorie=c)
        promo = Promotion.objects.create(date_debut=date.today(), date_fin=date.today(), pourcentage=10, produit=p)
        self.assertEqual(promo.pourcentage, 10)
        
    def test_create_produit(self):
        c = Categorie.objects.create(libelle="Légumes")
        p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", promotion=None, categorie=c)
        self.assertEqual(p.prix, 2.50)
        
    def test_create_admin(self):
        a = Admin.objects.create(nom="admin", mot_de_passe="password")
        self.assertEqual(a.nom, "admin")

'''
Test des méthodes date_debut_promo et date_fin_promo du modèle Promotion 
pour s'assurer que les dates sont correctement formatées

'''
class ModelTests(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(libelle="Légumes")
        
    def test_date_debut_promo(self):
        produit = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", promotion=None, categorie=self.categorie)
        p = Promotion.objects.create(date_debut=date(2023, 5, 1), date_fin=date(2023, 5, 31), pourcentage=10, produit=produit)
        self.assertEqual(p.date_debut_promo(), "1 mai 2023")
        
    def test_date_fin_promo(self):
        produit = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", promotion=None, categorie=self.categorie)
        p = Promotion.objects.create(date_debut=date(2023, 5, 1), date_fin=date(2023, 5, 31), pourcentage=10, produit=produit)
        self.assertEqual(p.date_fin_promo(), "31 mai 2023")

'''
Le test test_promo_creation() vérifie que l'objet créé est bien une instance de la 
classe Promo et que la méthode str() renvoie bien le titre de la promotion.

Le test test_promo_price() vérifie que la propriété "price" de l'objet Promo 
correspond bien à la valeur définie lors de la création de l'objet.

'''

class PromotionModelTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(libelle='test categorie')
        self.produit = Produit.objects.create(
            libelle='test produit',
            description='description',
            prix=10.00,
            image_url='https://example.com/image.jpg',
            categorie=self.categorie,
        )
        self.promo = Promotion.objects.create(
            date_debut='2023-06-01',
            date_fin='2023-06-30',
            pourcentage=10.0,
            produit=self.produit,
        )

    def test_promo_creation(self):
        self.assertTrue(isinstance(self.promo, Promotion))
        self.assertEqual(str(self.promo), self.produit.libelle)

    def test_promo_pourcentage(self):
        self.assertEqual(self.promo.pourcentage, 10.0)
        self.assertNotEqual(self.promo.pourcentage, 20.0)


