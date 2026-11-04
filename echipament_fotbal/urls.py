from django.urls import path
from . import views
from django.urls import path, re_path

urlpatterns = [
    path("",views.index, name="index"),
    path("info", views.info, name="info"),
    path("log", views.log, name="log"),
    path("istoric", views.istoric, name="istoric"),
    path("despre", views.despre, name="despre"),
    re_path(r"^accesare(?P<id>\d+)$", views.accesare, name="accesare"),
    path("produse", views.produse, name="produse"),
    path("contact", views.contact, name="contact"),
    path("cos_virtual", views.cos_virtual, name="cos_virtual"),
]