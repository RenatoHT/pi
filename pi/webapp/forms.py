from django import forms
from jsignature.widgets import JSignatureWidget
from jsignature.forms import JSignatureField
from django.core.validators import RegexValidator




class CreateNewForm(forms.Form):
    nome = forms.CharField(label="Nome Completo", max_length=200)
    data_nasc = forms.DateField(label="Data de Nascimento",
                                 widget=forms.DateInput(format="%d/%m/%Y" , attrs={'type': 'date'}))
    RG = forms.CharField(label="R.G.", 
                         max_length=12, 
                         validators=[RegexValidator(regex='[0-9]+',
                                                    message='somente números',)])
    CPF = forms.CharField(label="CPF",
                           max_length=14,
                           validators=[RegexValidator(regex='[0-9]+',
                                                    message='somente números',)])
    tel = forms.CharField(label="Telefone", 
                           validators=[RegexValidator(regex="""(55)?(?:([1-9]{2})?)(\d{4,5})(\d{4})$""",
                                                    message='erro',)])
    end = forms.CharField(label="Endereço")
    check = forms.BooleanField(label="Aceito")
    signature = JSignatureField(label="Assinatura",widget=JSignatureWidget(jsignature_attrs={'color': "#000000", 'height': '200px', 'width': '400px', "ResetButton":False}))
    