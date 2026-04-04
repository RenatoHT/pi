from django.shortcuts import render, HttpResponse
from .forms import CreateNewForm

# Create your views here.
def home(response):
    form = CreateNewForm()
    return render(response, "home.html", {'form':form})

def final(response):
    return HttpResponse("OK")
    