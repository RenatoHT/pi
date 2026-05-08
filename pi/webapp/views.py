from django.shortcuts import render, HttpResponse
from .forms import CreateNewForm
from .services import PDFgen
from .services import build_pairs
from pathlib import Path

# Create your views here.
def home(response):
    personal_fields = ['nome', 'data_nasc', 'rg', 'cpf', 'tel', 'endereco']

    if response.method == "POST":
        form = CreateNewForm(response.POST)

        if form.is_valid():
            print("IS VALID:", form.is_valid())
            print("ERRORS:", form.errors)
            return gerar_pdf(response, form, form.cleaned_data)
        else:
            print(form.errors)  # DEBUG
    else:
        form = CreateNewForm()

    fields = build_pairs(form)

    
    context = {
        "form": form,
        "personal_fields": personal_fields,
        "fields": fields
    }

    return render(response, "home.html", context)

def final(response):
    return HttpResponse("OK")

def gerar_pdf(request, form, data):
    BASE_DIR = Path(__file__).parent

    pdf_service = PDFgen(form, data)
    pdf = pdf_service.generate_pdf()

    return HttpResponse(pdf, content_type="application/pdf")
    