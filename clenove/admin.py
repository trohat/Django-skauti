from django.contrib import admin

# Register your models here.

from .models import Skaut, Oddil, AdresaKlubovny, Bobrik

class SkautAdmin(admin.ModelAdmin):
    #readonly_fields = ["slug"]
    prepopulated_fields = { "slug" : ("prezdivka", )}
    list_display = ["jmeno", "prezdivka", "splneno", "vek", "oddil"]
    list_filter = ["splneno", "vek", "oddil"]

class OddilAdmin(admin.ModelAdmin):
    list_display = ["jmeno", "seznam_skautu", "heslo"]

@admin.register(AdresaKlubovny)
class AdresaKlubovnyAdmin(admin.ModelAdmin):
    list_display = ["ulice", "cislo_popisne"]

@admin.register(Bobrik)
class BobrikAdmin(admin.ModelAdmin):
    list_display = ["nazev", "barva"]


admin.site.register(Skaut, SkautAdmin)
admin.site.register(Oddil, OddilAdmin)
