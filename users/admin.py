from django.contrib import admin

from .models import Needy, TypeWork, Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id_volunteer', 'pib_volunteer', 'phone', 'email', 'photo']
    search_fields = ['pib_volunteer', 'email']

admin.site.register(Needy)
admin.site.register(TypeWork)
admin.site.register(Volunteer)