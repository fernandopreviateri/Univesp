from django.db import models

# Create your models here.
class Paciente(models.Model):
    prontuario = models.CharField("Nome", max_length=255, blank = True, null = True)
    name = models.CharField("Nome", max_length=255, blank = True, null = True)
    dn = models.DateField('dn', blank = True, null = True)
    cpf = models.CharField("cpf", max_length=255, blank = True, null = True)
    message = models.TextField("mensagem", blank=True, null=True)
    createdAt = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.name