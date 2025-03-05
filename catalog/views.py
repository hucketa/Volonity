from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def catalog(request):
    return render(request, 'catalog/catalog.html')
