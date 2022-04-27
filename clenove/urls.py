from django.urls import path
from . import views

urlpatterns = [
    path("", views.uvod, name="uvod"),
    path("clenove/", views.clenove, name="clenove"),
    path("clenove/<int:cislo>", views.detail_clena, name="detail_clena")
]

