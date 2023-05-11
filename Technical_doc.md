Documentation Technique - Application Web de Promotions pour Mercadona

## Introduction

L'objectif de cette documentation technique est de présenter les éléments clés de l'application web de promotions pour Mercadona. Cette application est composée d'un front-end permettant aux utilisateurs de consulter les promotions, d'un back-end enregistrant les données dans une base de données PostgreSQL. Le back-end est développé en Python en utilisant Django, et le front-end utilise des templates HTML/CSS. Cette documentation abordera également la sécurité ainsi que les évolutions futures possibles de l'application.

## Architecture de l'application

L'application est structurée selon le modèle MVC (Modèle-Vue-Contrôleur), ce qui permet de séparer la logique de présentation de la logique de traitement des données. La structure globale de l'application est la suivante :

```
. 
|-- manage.py 
|-- mercadona  
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-39.pyc
|   |   |-- settings.cpython-39.pyc
|   |   |-- urls.cpython-39.pyc
|   |   `-- wsgi.cpython-39.pyc
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- mercadona_promos
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-39.pyc
|   |   |-- admin.cpython-39.pyc
|   |   |-- apps.cpython-39.pyc
|   |   |-- models.cpython-39.pyc
|   |   |-- urls.cpython-39.pyc
|   |   `-- views.cpython-39.pyc
|   |-- admin.py
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- __init__.py
|   |   `-- __pycache__
|   |       |-- 0001_initial.cpython-39.pyc
|   |       `-- __init__.cpython-39.pyc
|   |-- models.py
|   |-- static
|   |   |-- CSS
|   |   |   `-- style.css
|   |   |-- JS
|   |   |   `-- script.js
|   |   |-- android-chrome-192x192.png
|   |   |-- android-chrome-512x512.png
|   |   |-- apple-touch-icon.png
|   |   |-- favicon-16x16.png
|   |   |-- favicon-32x32.png
|   |   |-- favicon.ico
|   |   |-- images
|   |   |   `-- produits
|   |   |       |-- A13_150xp.jpg
|   |   `-- site.webmanifest
|   |-- templates
|   |   |-- base.html
|   |   |-- catalogue.html
|   |   |-- conditions.html
|   |   |-- confidentialites.html
|   |   `-- mentions.html
|   |-- templatetags
|   |   `-- custom_filters.py
|   |-- tests
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   |-- __init__.cpython-39.pyc
|   |   |   |-- test_models.cpython-39.pyc
|   |   |   `-- test_views.cpython-39.pyc
|   |   |-- test_models.py
|   |   `-- test_views.py
|   |-- urls.py
|   `-- views.py
|-- requirements.txt
```

Le dossier `mercadona_promos` contient les fichiers de configuration de l'application avec les modèles et les vues pour la gestion des produits. Les dossiers `static` et `static/images` contiennent respectivement les fichiers statiques (CSS, JS) et les fichiers médias (images).

## Sécurité

L'application web de promotions pour Mercadona doit respecter les principes de sécurité suivants :

1. Authentification des utilisateurs : seuls les administrateurs peuvent ajouter des promotions sur des produits. L'authentification est mise en place grâce au système d'authentification intégré de Django, qui utilise des sessions pour stocker les informations d'authentification.
2. Protection contre les attaques CSRF : les formulaires de l'application incluent des jetons CSRF pour empêcher les attaques CSRF (Cross-Site Request Forgery).
3. Protection contre les attaques XSS : les données entrées par les utilisateurs sont échappées pour empêcher les attaques XSS (Cross-Site Scripting).
4. Protection de la base de données : les mots de passe des utilisateurs sont stockés de manière sécurisée en utilisant un algorithme de hachage et de salage.
5. Mises à jour régulières : les mises à jour de sécurité pour le système d'exploitation, la base de données et les bibliothèques Python sont effectuées régulièrement pour garantir la sécurité de l'application.

Évolutions futures
Plusieurs évolutions sont envisageables pour améliorer l'application web de promotions pour Mercadona :

* Ajouter une fonctionnalité de recherche pour les promotions et les produits.
* Mettre en place une gestion des stocks pour les produits en promotion.
* Intégrer un système de notifications pour informer les utilisateurs des nouvelles promotions.
* Améliorer l'interface utilisateur pour rendre l'application plus conviviale et intuitive.
* Ajouter une fonctionnalité de recommandation de produits basée sur les achats précédents de l'utilisateur.

Conclusion :
L'application web de promotions Mercadona est une application robuste et sécurisée développée en utilisant les technologies les plus récentes. Elle offre une expérience utilisateur agréable et permet une gestion efficace des promotions pour les administrateurs. Les évolutions futures envisagées permettront d'améliorer encore davantage l'application et d'offrir des fonctionnalités supplémentaires aux utilisateurs.
