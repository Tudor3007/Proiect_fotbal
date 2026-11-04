from django.db import models


class Brand(models.Model):
    nume = models.CharField(
        max_length=50,
        unique=True,
        help_text="Numele brandului (ex: Nike, Adidas)",
        error_messages={"unique": "Exista deja un brand cu acest nume."},
    )
    tara_origine = models.CharField(max_length=50, null=True, blank=True)
    an_infiintare = models.PositiveIntegerField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Branduri"
        ordering = ["nume"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(an_infiintare__gte=1800) & models.Q(an_infiintare__lte=2026),
                name="brand_an_valid",
                violation_error_message="Anul trebuie sa fie intre 1800 si 2026.",
            ),
        ]

    def __str__(self):
        return self.nume


class Categorie(models.Model):
    nume = models.CharField(
        max_length=50,
        unique=True,
        help_text="Numele categoriei (ex: Ghete, Tricouri)",
        error_messages={"unique": "Exista deja o categorie cu acest nume"}
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )
    descriere = models.TextField(null=True, blank=True)
    culoare = models.CharField(
        max_length=7,
        default="#000000",
        help_text="Culoarea categoriei (ex: #FF0000)"
    )
    sigla = models.ImageField(
        upload_to="categorii/",
        null=True,
        blank=True,
    )
    ordine_afisare = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categorii"
        ordering = ["ordine_afisare"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(ordine_afisare__gte=0),
                name="categorii_ordine_afisare",
                violation_error_message="Numarul trebuie sa fie mai mare sau egal cu 0"
            ),
        ]

    def __str__(self):
        return self.nume


class Magazin(models.Model):
    nume = models.CharField(
        max_length=100,
        help_text="Numele magazinului (ex: Goal Gear Centru)",
        error_messages={"max_length": "Lungimea maxima a textului este depasita"},
    )
    adresa = models.CharField(
        max_length=200,
        help_text="Adresa magazinului",
    )
    oras = models.CharField(
        max_length=50,
        help_text="Oras",
    )
    telefon = models.CharField(
        max_length=15,
        error_messages={"max_length": "Numarul de telefon este prea lung"}
    )
    data_deschidere = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Magazine"
        ordering = ["oras", "nume"]

    def __str__(self):
        return f"{self.nume} ({self.oras})"
