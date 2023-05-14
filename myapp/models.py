from django.db import models

class Opskrifter(models.Model):
    title = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    Oprettet_dato = models.DateField('Dato oprettet')

class MiesOpskrifter(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, null=True, blank=True)
    kitchen = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    tested = models.BooleanField(default=False, null=True, blank=True)
    deleted = models.BooleanField(default=False)




