from django.db import models

# Create your models here.
class Proizvod(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    cena = models.FloatField()
    kolicina_na_stanju = models.PositiveIntegerField(default=0)
    opis = models.TextField()

class Sporet(models.Model):
    proizvod = models.ForeignKey('Proizvod', on_delete=models.CASCADE)
    TIPOVI = (
        ('RP', 'Ravna Ploca'),
        ('ST', 'Standardni')
    )
    tip = models.CharField(max_length=2, choices = TIPOVI, default='ST')
    ostalo = models.TextField()