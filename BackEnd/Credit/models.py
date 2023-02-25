from django.db import models

# Create your models here.

class Demande(models.Model):
    DemandeId=models.AutoField(primary_key=True)
    ClientId=models.IntegerField()
    Montant=models.IntegerField()
    Status=models.CharField(max_length=100)
    But=models.CharField(max_length=100)
