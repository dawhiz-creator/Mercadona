from django.test import TestCase, Client
from django.urls import reverse
# from .models import Produit, Categorie, Promotion
from mercadona_promos.models import Produit, Categorie, Promotion


'''
Crée une instance de la classe Client pour tester la vue, puis définit l'URL de la 
vue "catalogue". Dans la méthode setUp(), il crée également des instances de Produit, 
Categorie et Promotion pour tester l'affichage des données.

&
teste si la réponse de la vue "catalogue" est correcte. Elle vérifie si le code 
d'état de la réponse est 200, si le bon modèle est utilisé, et si toutes les données 
attendues sont présentes dans la réponse, telles que le nom et la description du 
produit, le prix avant et après promotion, la catégorie, l'image du produit, etc.

Enfin, elle vérifie également si les sections "Les Bons Plans", "Filtrer par catégorie"
et "Promotions en cours" sont présentes dans la réponse et contiennent les données 
attendues.

'''

# class TestCatalogueView(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.catalogue_url = reverse('catalogue')
        
#         self.categorie = Categorie.objects.create(libelle='test_categorie')
#         self.produit = Produit.objects.create(
#             libelle='test_produit',
#             description='test_description',
#             categorie=self.categorie,
#             prix=10,
#             image_url='test_image_url'
#         )
#         self.promotion = Promotion.objects.create(
#             produit=self.produit,
#             pourcentage=50,
#             date_debut='2023-05-01',
#             date_fin='2023-05-31'
#         )
        
#     def test_catalogue_view_GET(self):
#         response = self.client.get(self.catalogue_url)
        
#         self.assertRedirects(response, 'https://testserver/', status_code=301, target_status_code=200)
        
#         # Si la redirection a fonctionné, le code ci-dessous sera exécuté
        
#         self.assertTemplateUsed(response, '../templates/catalogue.html')
        
#         print(response.content) # Afficher le contenu de la réponse

        
#         self.assertContains(response, 'test_produit')
#         self.assertContains(response, 'test_description')
#         self.assertContains(response, 'test_categorie')
#         self.assertContains(response, '10 €')
#         self.assertContains(response, '5 €')
#         self.assertContains(response, 'test_image_url')
        
#         self.assertContains(response, 'Les Bons Plans')
#         self.assertNotContains(response, 'Aucun produit en promotion pour le moment.')
        
#         self.assertContains(response, 'Filtrer par catégorie')
#         self.assertContains(response, 'test_categorie')
        
#         self.assertContains(response, 'Promotions en cours')
#         self.assertContains(response, 'test_produit')
#         self.assertContains(response, '50% de réduction')
#         self.assertContains(response, '01 mai 2023')
#         self.assertContains(response, '31 mai 2023')
