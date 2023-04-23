Documentation Technique - Application Web de Promotions pour Mercadona

## Introduction

L'objectif de cette documentation technique est de présenter les éléments clés de l'application web de promotions pour Mercadona. Cette application est composée d'un front-end permettant aux utilisateurs de consulter les promotions, d'un back-end enregistrant les données dans une base de données PostgreSQL. Le back-end est développé en Python en utilisant Django, et le front-end utilise des templates HTML/CSS. Cette documentation abordera également la sécurité ainsi que les évolutions futures possibles de l'application.

## Architecture de l'application

L'application est structurée selon le modèle MVC (Modèle-Vue-Contrôleur), ce qui permet de séparer la logique de présentation de la logique de traitement des données. La structure globale de l'application est la suivante :

application/
    __init__.py
    settings.py
    urls.py
    wsgi.py
catalogue/
    __init__.py
    admin.py
    apps.py
    models.py
    views.py
    templates/
        catalogue/
            index.html
            detail.html
    tests/
        __init__.py
        test_views.py
        test_models.py
promotions/
    __init__.py
    admin.py
    apps.py
    models.py
    views.py
    templates/
        promotions/
            add.html
            edit.html
    tests/
        __init__.py
        test_views.py
        test_models.py
users/
    __init__.py
    admin.py
    apps.py
    forms.py
    models.py
    views.py
    templates/
        users/
            login.html
    tests/
        __init__.py
        test_views.py
        test_models.py
static/
    css/
    js/
media/

Le dossier `application` contient les fichiers de configuration de l'application. Le dossier `catalogue` contient les modèles et les vues pour la gestion des produits. Le dossier `promotions` contient les modèles et les vues pour la gestion des promotions. Le dossier `users` contient les modèles, les vues et les formulaires pour la gestion des utilisateurs et de l'authentification. Les dossiers `static` et `media` contiennent respectivement les fichiers statiques (CSS, JS) et les fichiers médias (images).

## Sécurité

L'application web de promotions pour Mercadona doit respecter les principes de sécurité suivants :

1. Authentification des utilisateurs : seuls les administrateurs peuvent ajouter des promotions sur des produits. L'authentification est mise en place grâce au système d'authentification intégré de Django, qui utilise des sessions pour stocker les informations d'authentification.
2. Protection contre les attaques CSRF : les formulaires de l'application incluent des jetons CSRF pour empêcher les attaques CSRF (Cross-Site Request Forgery).
3. Protection contre les attaques XSS : les données entrées par les utilisateurs sont échappées pour empêcher les attaques XSS (Cross-Site Scripting).
4. Protection de la base de données : les mots de passe des utilisateurs sont stockés de manière sécurisée en utilisant un algorithme de hachage et de salage.
5. Mises à jour régulières : les mises à jour de sécurité pour le système d'exploitation, la base de données et les bibliothèques Python

sont effectuées régulièrement pour garantir la sécurité de l'application.

Évolutions futures
Plusieurs évolutions sont envisageables pour améliorer l'application web de promotions pour Mercadona :

* Ajouter une fonctionnalité de recherche pour les promotions et les produits.
* Mettre en place une gestion des stocks pour les produits en promotion.
* Intégrer un système de notifications pour informer les utilisateurs des nouvelles promotions.
* Améliorer l'interface utilisateur pour rendre l'application plus conviviale et intuitive.
* Ajouter une fonctionnalité de recommandation de produits basée sur les achats précédents de l'utilisateur.

Conclusion
L'application web de promotions Mercadona est une application robuste et sécurisée développée en utilisant les technologies les plus récentes. Elle offre une expérience utilisateur agréable et permet une gestion efficace des promotions pour les administrateurs. Les évolutions futures envisagées permettront d'améliorer encore davantage l'application et d'offrir des fonctionnalités supplémentaires aux utilisateurs.
