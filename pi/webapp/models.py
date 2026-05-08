from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=200)
    tel = models.CharField(max_length=15)
    data_nasc = models.DateField()
    rg = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=300)
    

    alergia_bool = models.BooleanField(default=False)
    alergia_str = models.CharField(max_length=200, blank=True)

    hepatite_bool = models.BooleanField(default=False)
    hepatite_str = models.CharField(max_length=200, blank=True)

    hiv_bool = models.BooleanField(default=False)
    hiv_str = models.CharField(max_length=200, blank=True)

    gravida_bool = models.BooleanField(default=False)
    gravida_str = models.CharField(max_length=200, blank=True)

    amamentando_bool = models.BooleanField(default=False)
    amamentando_str = models.CharField(max_length=200, blank=True)

    diabetes_bool = models.BooleanField(default=False)
    diabetes_str = models.CharField(max_length=200, blank=True)

    hipertensao_bool = models.BooleanField(default=False)
    hipertensao_str = models.CharField(max_length=200, blank=True)

    probcard_bool = models.BooleanField(default=False)
    probcard_str = models.CharField(max_length=200, blank=True)

    probresp_bool = models.BooleanField(default=False)
    probresp_str = models.CharField(max_length=200, blank=True)

    depre_bool = models.BooleanField(default=False)
    depre_str = models.CharField(max_length=200, blank=True)

    acne_bool = models.BooleanField(default=False)
    acne_str = models.CharField(max_length=200, blank=True)

    trombvari_bool = models.BooleanField(default=False)
    trombvari_str = models.CharField(max_length=200, blank=True)

    herpes_bool = models.BooleanField(default=False)
    herpes_str = models.CharField(max_length=200, blank=True)
    
    ilicita_bool = models.BooleanField(default=False)
    ilicita_str = models.CharField(max_length=200, blank=True)

    medicamento_bool = models.BooleanField(default=False)
    medicamento_str = models.CharField(max_length=200, blank=True)

    dente_bool = models.BooleanField(default=False)
    dente_str = models.CharField(max_length=200, blank=True)

    injeta_bool = models.BooleanField(default=False)
    injeta_str = models.CharField(max_length=200, blank=True)

    proce_bool = models.BooleanField(default=False)
    proce_str = models.CharField(max_length=200, blank=True)

    plastica_bool = models.BooleanField(default=False)
    plastica_str = models.CharField(max_length=200, blank=True)

    doenca_bool = models.BooleanField(default=False)
    doenca_str = models.CharField(max_length=200, blank=True)

    infoadd = models.CharField(max_length=200, blank=True)

    assinatura = models.ImageField(null=True, blank=True)



