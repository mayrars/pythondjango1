from django.db import models
from django.utils.html import format_html

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto="{0} ({1})".format(self.nombre, self.creditos)
        return texto
    
    def coloreado(self):
        if self.creditos >= 4:
            return format_html("<span style='color:blue'>{0}</span>".format(self.nombre))
        else:
            return format_html("<span style='color:red'>{0}</span>".format(self.nombre))
