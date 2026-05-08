from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    data_nasc = models.DateField()
    assinatura = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nome