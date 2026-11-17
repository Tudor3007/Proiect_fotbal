from django.conf import settings
from .models import Categorie

def date_firma(request):
    return {
        "firma": settings.FIRMA,
    }

def categorii_meniu(request):
    return {
        "categorii_meniu": Categorie.objects.filter(produs__isnull=False).distinct(),
    }