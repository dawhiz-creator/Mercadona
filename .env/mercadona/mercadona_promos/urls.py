from django.urls import path
from . import views

# images
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
        # path('produit/<int:produit_id>/', views.detail_produit, name='detail-produit'),

]

# images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
