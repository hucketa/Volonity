from django.db import models

from users.models import Needy
from users.models import TypeWork
from users.models import Volunteer

class Request(models.Model):
    id_needy = models.ForeignKey(Needy, on_delete=models.CASCADE)  # Зв'язок з Needy
    code_type_work = models.ForeignKey(TypeWork, on_delete=models.CASCADE)  # Зв'язок з TypeWork
    execution_date = models.DateField()  # Дата виконання
    problem_description = models.TextField()  # Опис проблеми
    code_request = models.IntegerField(primary_key=True)  # Код заявки

    def __str__(self):
        return str(self.code_request)

class Service(models.Model):
    id_service = models.IntegerField(primary_key=True)  # Первинний ключ
    code_request = models.ForeignKey(Request, on_delete=models.CASCADE)  # Зв'язок з Request
    execution_date = models.DateField()  # Дата виконання
    id_volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)  # Зв'язок з Volunteer

    def __str__(self):
         return f"Послуга {self.id_service} для заявки {self.code_request.code_request}"
