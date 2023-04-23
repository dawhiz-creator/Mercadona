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
