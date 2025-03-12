from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Needy, Volunteer, TypeWork
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Перевіряємо, чи є користувач в таблиці Needy
        needy_user = Needy.objects.filter(email=email).first()
        if needy_user and needy_user.password == password:  # Якщо паролі незахешовані
            request.session['user_email'] = email  # Зберігаємо email в сесії
            return redirect("catalog_service")  # Перенаправлення для Needy

        # Перевіряємо, чи є користувач в таблиці Volunteer
        volunteer_user = Volunteer.objects.filter(email=email).first()
        if volunteer_user and volunteer_user.password == password:
            request.session['user_email'] = email  # Зберігаємо email в сесії
            return redirect("catalog")  # Перенаправлення для Volunteer

        # Якщо користувача не знайдено або пароль неправильний
        return render(request, "users/login.html", {"error": "Невірний email або пароль"})

    return render(request, "users/login.html")

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']


        
        is_volunteer = request.POST.get('is_volunteer', False)

        # Перевірка на існування користувача з таким email
        if User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'error': 'Такий email вже зареєстрований'})

        # Створення нового користувача
        user = User.objects.create_user(username=email, email=email, password=password)

        request.session['user_email'] = email


        if is_volunteer:

            try:
                type_work = TypeWork.objects.get(code_type_work=1)  # Заміни на потрібний id
            except TypeWork.DoesNotExist:
                type_work = None
            # Створення волонтера
            volunteer_count = Volunteer.objects.count() + 1
            volunteer = Volunteer(
                id_volunteer=volunteer_count,
                email=email,
                password=password,
                login=email,
                phone=0,
                amount_of_help=0,  # За замовчуванням
                code_type_work=type_work,  # Можна передати конкретний тип роботи
            )
            volunteer.save()

            # Перенаправляємо на сторінку catalog
            return redirect("catalog")  # Перевір, чи маєш URL з ім'ям 'catalog'
        else:
            # Створення потребуючого
            needy_count = Needy.objects.count() + 1
            needy = Needy(
                id_needy=needy_count,
                email=email,
                password=password,
                login=email,
                phone=0,  # Буде заповнено пізніше
                pib_needy="",  # Заповниться пізніше
            )
            needy.save()

            # Перенаправляємо на сторінку catalog_service
            return redirect("catalog_service")
    return render(request, "users/register.html")

def catalog_service(request):
    return render(request, "catalog/catalog_service.html")  # Відображаємо шаблон catalog_service.html

def catalog(request):
    return render(request, "catalog/catalog.html")  # Відображаємо шаблон catalog.html
