from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class AdresaKlubovny(models.Model):
    ulice = models.CharField(max_length=100)
    cislo_popisne = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Adresy kluboven"

    def __str__(self):
        return f"{self.ulice} {self.cislo_popisne}"

class Oddil(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    heslo = models.CharField(max_length=300)
    klubovna = models.OneToOneField(AdresaKlubovny, on_delete=models.SET_NULL, null=True)

    def seznam_skautu(self):
        return [skaut.jmeno for skaut in self.skauti.all()]

    class Meta:
        verbose_name_plural = "Oddíly"
        verbose_name = "Oddíl"

    def __str__(self):
        return self.jmeno

class Bobrik(models.Model):
    nazev = models.CharField(max_length=100)
    barva = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Bobříci"

    def __str__(self):
        return self.nazev

class Skaut(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    prezdivka = models.CharField("Přezdívka",
        help_text="Prosím, zadávejte bez diakritiky",
        max_length=100)
    vek = models.IntegerField("Věk")
    slug = models.SlugField()
    splneno = models.BooleanField("Splněno", default=False, help_text="Už splnil skautskou zkoušku?")
    oddil = models.ForeignKey(Oddil,
        verbose_name="Oddíl",
        on_delete=models.CASCADE,
        null=True,
        related_name="skauti"
    )
    bobrici = models.ManyToManyField(Bobrik, related_name="skauti")

    def get_absolute_url(self):
        return reverse("detail_clena", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prezdivka)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.jmeno} - {self.prezdivka}"

    class Meta:
        verbose_name_plural = "Skauti"

# positional arguments
# keyword arguments