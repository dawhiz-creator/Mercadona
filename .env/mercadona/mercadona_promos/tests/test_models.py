'''
création d'objets Categorie, Promotion, Produit et Admin pour s'assurer 
qu'ils sont correctement stockés dans la base de données
'''

from datetime import date
from django.test import TestCase
from mercadona_promos.models import Categorie, Promotion, Produit, Admin


                                #    Test OK
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


                         #    Test OK

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



                                 #    Test échoué

'''
Test de la méthode prix_apres_promo du modèle Produit 
pour s'assurer que les calculs de prix sont corrects
'''
# # class ProduitModelTests(TestCase):
# #     def test_prix_apres_promo_without_promo(self):
# #         c = Categorie.objects.create(libelle="Légumes")
# #         p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", promotion=None, categorie=c)
# #         self.assertEqual(p.prix_apres_promo(), "2.50")
        
# #     def test_prix_apres_promo_with_promo(self):
# #         c = Categorie.objects.create(libelle="Légumes")
# #         p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=2.50, image_url="", categorie=c)
# #         promo = Promotion.objects.create(date_debut=date.today(), date_fin=date.today(), pourcentage=10, produit=p)
# #         print("Produit avant la promo :", p.prix)
# #         print("Produit après la promo :", p.prix_apres_promo())
# #         self.assertEqual(p.prix_apres_promo(), "2.25")


#----------------------TEST en cours FIN-----------#







'''
Testez la méthode image du modèle Produit pour s'assurer que les images
sont correctement récupérées depuis l'URL

'''
# class ModelTests(TestCase):
#     def test_image_with_url(self):
#         c = Categorie.objects.create(libelle="Légumes")
#         p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches",prix=1.99, categorie=c, image_url="https://www.example.com/carrots.jpg")
#           # Vérifiez que la méthode image renvoie bien l'URL de l'image du produit
#         self.assertEquals(p.image(), "https://www.example.com/carrots.jpg")

from django.core.files import File
from django.test import TestCase
from mercadona_promos.models import Categorie, Produit

class ModelTests(TestCase):
    def test_image_with_url(self):
        c = Categorie.objects.create(libelle="Légumes")
        with open('static/images/produits/A13_150_.jpg', 'rb') as f:
            p = Produit.objects.create(libelle="Carottes", description="Des carottes fraîches", prix=1.99, categorie=c)
            p.image.save('A13_150_.jpg', File(f))
            # Vérifiez que la méthode image renvoie bien l'URL de l'image du produit
            self.assertEquals(p.image.url, '/media/A13_150_.jpg')



'''
Le test test_promo_creation() vérifie que l'objet créé est bien une instance de la 
classe Promo et que la méthode str() renvoie bien le titre de la promotion.

Le test test_promo_price() vérifie que la propriété "price" de l'objet Promo 
correspond bien à la valeur définie lors de la création de l'objet.

'''


        #    Test OK
from django.test import TestCase
from mercadona_promos.models import Produit, Promotion, Categorie


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
