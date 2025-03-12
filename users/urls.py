from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("catalog_service/", views.catalog_service, name="catalog_service"),
    path("catalog/", views.catalog, name="catalog"),
    path('register/', views.register, name='register'),
]
