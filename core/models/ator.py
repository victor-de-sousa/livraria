from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'ator'
        verbose_name_plural = 'atores'

    def __str__(self):
        return self.nome