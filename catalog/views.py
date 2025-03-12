from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Request
from .models import Service
from .models import Volunteer
from .models import Needy
from django.conf import settings

@login_required
def catalog(request):
    return render(request, 'catalog/catalog.html')

def profile_volunteer(request):
    return render(request, 'profile1/profile_volunteer.html')

def profile_needy(request):
    return render(request, 'profile1/profile_needy.html')

def specialists_list(request):
    requests = Request.objects.all()
    print(requests)
    return render(request, 'catalog/catalog.html', {'requests': requests})

def catalog_view(request):
    requests = Request.objects.all() 
    return render(request, 'catalog/catalog.html', {'requests': requests})


def catalog_service_view(request):
    services = Service.objects.select_related('code_request', 'id_volunteer').all()
    # Отримуємо поточного користувача за електронною поштою
    user_email = request.session.get('user_email')
    
    try:
        needy = Needy.objects.get(email=user_email)
    except Needy.DoesNotExist:
        needy = None

    if needy:
        # Отримуємо всі заявки цього користувача
        requests = Request.objects.filter(id_needy=needy)
        # Отримуємо всі послуги, що відповідають цим заявкам
        services = Service.objects.filter(code_request__in=requests)
    else:
        services = []
    return render(request, 'catalog/catalog_service.html', {'services': services, 'MEDIA_URL': settings.MEDIA_URL})

#def catalog_service_view(request):
   # services = Service.objects.all()
   # volunteers = Volunteer.objects.all()
    #return render(request, 'catalog/catalog_service.html', {'services': services, 'volunteers': volunteers, 'MEDIA_URL': settings.MEDIA_URL})