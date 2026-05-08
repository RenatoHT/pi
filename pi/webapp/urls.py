from django.urls import path
from . import views

urlpatterns =  [
    path("", views.home, name="home"),
    path("gerar_pdf/", views.gerar_pdf, name="pdf")
]