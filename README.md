# Mercadona Retail App

## Description

Cette application web permet à l'utilisateur de consulter les promotions de Mercadona, une entreprise de retail disposant de 1675 magasins en Espagne.

## Fonctionnalités

* Authentification pour les administrateurs
* Ajout de produits avec libellé, description, prix, image et catégorie
* Mise en promotion des produits avec pourcentage de remise et dates de début et de fin
* Affichage de tous les produits, y compris ceux sans promotion, dans l'onglet "catalogue"
* Filtre pour afficher les produits par catégorie
* Affichage des produits en promotion avec leur nouveau prix en gras et rouge

## Installation

1. Cloner le repository : `git clone https://github.com/votre-repository`
2. Installer les dépendances : `pip install -r requirements.txt`
3. Configurer les variables d'environnement : `cp .env.example .env`
4. Exécuter les migrations de la base de données : `python manage.py migrate`
5. Exécuter le serveur de développement : `python manage.py runserver`

## Configuration

Les variables d'environnement suivantes doivent être configurées :

* `SECRET_KEY`: la clé secrète pour Django
* `DEBUG`: si `True`, active le mode debug de Django (non conseillé pour la Prod)
* `DATABASE_URL`: l'URL de la base de données PostgreSQL

## Utilisation

1. Accéder à l'application à l'adresse `http://localhost:8000 ` en local ou sur [Site internet de Mercadona](https://mercadona-retail.fly.dev/)
2. Se connecter en tant qu'administrateur pour ajouter des promotions et modifier les produits

## Exemples

* Ajouter un produit :

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>markdown</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-markdown">1. Créer un produit depuis l'espace admin avec un libellé, une description, un prix, une image et une catégorie
2. Accéder au catalogue et cliquer sur le bouton "promotion" pour le produit ajouté
3. appliquer le libelle de promotion à appliquer (les dates de début et de fin de la promotion définies lors de la création de cette promotion s'afficheront et le pourcentage automatiquement appliqué au produit)
	- un produit peut se faire appliquer la promotion destinée à un autre produit (dans ce cas il ne s'affichera pas dans les blocs bons-plans et promotions-en-cours), cette promotion s'affichera uniquement dans la catégorie correspondante à ce produit ou dans le catalogue global
        - pour faire apparaître un produit dans les blocs bons-plans et promotions-en-cours, il faut créer la promotion de ce produit et la lui appliquer
4. Le nouveau prix est calculé automatiquement et la promotion est appliquée
</code></div></div></pre>

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à créer une issue ou une pull request.

## Licence

Cette application est distribuée sous la licence MIT.

## Auteurs

* Dawhiz-creator

## Contact

Pour toute question ou assistance, veuillez envoyer un e-mail à [support@mercadona-retail.com](mailto:dawhiz@live.fr).

## Liens utiles

* [Site internet de Mercadona](https://mercadona-retail.fly.dev/) : Site officiel de Mercadona.
