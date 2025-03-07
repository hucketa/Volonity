from django.contrib import admin

from .models import Needy, TypeWork, Volunteer

admin.site.register(Needy)
admin.site.register(TypeWork)
admin.site.register(Volunteer)