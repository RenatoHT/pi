from weasyprint import HTML
from django.template.loader import render_to_string

class TermoConsentimentoPDF:
    template_name = "termo.html"

    def __init__(self, data: dict):
        self.data = data

    def render_html(self) -> str:
        return render_to_string(self.template_name, self.data)

    def generate_pdf(self) -> bytes:
        html_string = self.render_html()
        return HTML(string=html_string).write_pdf()

    def save(self, path: str):
        pdf_bytes = self.generate_pdf()
        with open(path, "wb") as f:
            f.write(pdf_bytes)


data = {
    "name": "João da Silva",
    "birthdate": "01/01/1990",
    "rg": "12.345.678-9",
    "cpf": "123.456.789-00",
    "telefone": "(11) 99999-9999",
    "endereco": "Rua Exemplo, 123 - São Paulo",
    "cidade": "São Paulo",
    "dia": "05",
    "mes": "Maio",
}

pdf = TermoConsentimentoPDF(data)
pdf.save("termo.pdf")