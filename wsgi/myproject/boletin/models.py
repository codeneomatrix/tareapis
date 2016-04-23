from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre= models.CharField(max_length=120,blank=False)
    tema= models.CharField(max_length=120,blank=False)
    email = models.EmailField()

    def __unicode__(self):
        return self.email
