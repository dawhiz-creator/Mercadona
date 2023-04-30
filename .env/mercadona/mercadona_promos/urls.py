# from django.urls import path
# from . import views


# urlpatterns = [
#     path('mercadona_promos', views.catalogue, name='catalogue'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
]
# images

# urlpatterns = [
#     # vos vues ici
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
