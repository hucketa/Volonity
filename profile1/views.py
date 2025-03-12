from django.shortcuts import render
from users.models import Needy, Volunteer
from django.conf import settings

def profile_needy_view(request):
    # Отримуємо електронну пошту користувача з сесії
    user_email = request.session.get('user_email')
    print(f"User email from session: {user_email}")

    if not user_email:
        return redirect('login')  # Якщо користувач не залогінений, перенаправляємо на сторінку логіну

    # Отримуємо користувача з таблиці Needy
    try:
        needy_user = Needy.objects.get(email=user_email)
    except Needy.DoesNotExist:
        needy_user = None

    if not needy_user:
        return render(request, 'users/login.html', {'error': 'Користувача не знайдено'})

    # Передаємо дані користувача на шаблон
    return render(request, 'profile1/profile_needy.html', {'needy_user': needy_user, 'MEDIA_URL': settings.MEDIA_URL})

def profile_volunteer_view(request):
    # Отримуємо електронну пошту користувача з сесії
    user_email = request.session.get('user_email')
    #print(f"User email from session: {user_email}")

    if not user_email:
        return redirect('login')  # Якщо користувач не залогінений, перенаправляємо на сторінку логіну

    # Отримуємо користувача
    try:
        volunteer_user = Volunteer.objects.get(email=user_email)
    except Volunteer.DoesNotExist:
        volunteer_user = None

   # if not volunteer_user:
        #return render(request, 'users/login.html', {'error': 'Користувача не знайдено'})

    # Передаємо дані користувача на шаблон
    return render(request, 'profile1/profile_volunteer.html', {'volunteer_user': volunteer_user, 'MEDIA_URL': settings.MEDIA_URL})