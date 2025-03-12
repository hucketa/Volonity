from django.urls import path
from . import views
from .views import catalog_view
from .views import catalog_service_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('profile1/', views.profile_volunteer, name='profile_volunteer'),
    path('profile1/', views.profile_needy, name='profile_needy'),
    path('specialists/', views.specialists_list, name='specialists_list'),
    path('catalog/', catalog_view, name='catalog'), 
    path('services/', catalog_service_view, name='catalog_service'),
path('catalog/services/', views.catalog_service_view, name='catalog_services'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
