from django.db import models

# Create your models here.

class Skaut(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    prezdivka = models.CharField("Přezdívka",
        help_text="Prosím, zadávejte bez diakritiky",
        max_length=100)
    vek = models.IntegerField("Věk")
    splneno = models.BooleanField("Splněno", default=False, help_text="Už splnil skautskou zkoušku?")

    def __str__(self):
        return f"{self.jmeno} - {self.prezdivka}"

    class Meta:
        verbose_name_plural = "Skauti"

# positional arguments
# keyword arguments