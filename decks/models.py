from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deck(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=300)
    enlace = models.URLField(max_length=256, null=True, blank=True)
    formato = models.CharField(max_length=50, choices=[('Standard', 'Standard'), ('Modern', 'Modern'), ('Commander', 'Commander')])
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)
