from django.contrib import admin
from .models import Brand, Categorie, Magazin, Produs, Raion, DisponibilIn
from django.utils.html import format_html
import csv
from django.http import HttpResponse

admin.site.site_title = "Goal Gear Admin"
admin.site.site_header = "Administrare Goal Gear"
admin.site.index_title = "Panou de control"
admin.site.site_url = "/echipament_fotbal/"

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ["nume","tara_origine"]
    search_help_text = "Cautati dupa numele sau tara de origine a brandului"


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ["nume","slug"]
    search_help_text = "Cautati dupa numele sau dupa slugul categoriei"

@admin.register(Magazin)
class MagazinAdmin(admin.ModelAdmin):
    search_fields = ["nume", "oras"]
    search_help_text = "Cautati dupa numele sau orasul magazinului"

@admin.register(Raion)
class RaionAdmin(admin.ModelAdmin):
    search_fields = ["nume","magazin__nume"]
    search_help_text = "Cautati dupa numele raionului sau al magazinului caruia ii apartine"

@admin.register(DisponibilIn)
class DisponibilInAdmin(admin.ModelAdmin):
    search_fields = ["produs__nume", "magazin__nume"]
    search_help_text = "Cautati dupa numele produsului sau al magazinului in care este disponibil"



@admin.register(Produs)
class ProdusAdmin(admin.ModelAdmin):
    list_display = ["nume", "pret_formatat", "categorie", "brand", "tara_brand"]
    search_fields = ["nume","gen"]
    search_help_text = "Cautati dupa numele sau genul produsului"
    ordering = ["-pret"]
    list_filter = ["categorie", "gen", "in_promotie", "brand"]
    list_per_page = 5
    fieldsets = (
    ("Date Principale", {
        "fields": ("nume", "pret", "categorie", "gen", "in_promotie")
    }),
    ("Informatii suplimentare", {
        "fields": ("descriere", "culoare", "marimi_disponibile", "brand"),
        "classes": ("collapse",),
    })
    )
    actions = ["exporta_csv", "pune_la_promotie", "scoate_din_promotie"]

    @admin.action(description="Exporta produsele selectate in CSV")
    def exporta_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=produse.csv"
        writer = csv.writer(response)
        writer.writerow(["Nume","Pret", "Categorie", "Brand"])
        for p in queryset:
            writer.writerow([p.nume, p.pret, p.categorie, p.brand.nume])
        return response

    @admin.action(description="Pune produsele selectate la promotie")
    def pune_la_promotie(self, request, queryset):
        nr=queryset.update(in_promotie=True)
        self.message_user(request, f"{nr} produse au fost puse la promotie.")

    @admin.action(description="Scoate produsele selectate de la promotie")
    def scoate_din_promotie(self, request, queryset):
        nr = queryset.update(in_promotie=False)
        self.message_user(request, f"{nr} produse au fost scoase de la promotie.")

    @admin.display(description="Tara brand")
    def tara_brand(self, obj):
        return obj.brand.tara_origine if obj.brand else "-"

    @admin.display(description="Pret", ordering="pret")
    def pret_formatat(self, obj):
        if obj.in_promotie:
            return format_html('<b style="color: {};">{} lei - PROMO</b>', "green", obj.pret)
        return format_html('<b style="color: {};">{} lei</b>', "red", obj.pret)