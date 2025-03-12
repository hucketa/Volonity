from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('profile_needy/', views.profile_needy_view, name='profile_needy'),
  path('profile_volunteer/', views.profile_volunteer_view, name='profile_volunteer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
