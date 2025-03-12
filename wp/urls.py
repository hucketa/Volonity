from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('accounts/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('profile1/', include('profile1.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

