from __future__ import unicode_literals

from django.db import models

class Persona(models.Model):
    id_per = models.AutoField(primary_key=True)
    per_id = models.CharField(unique=True, max_length=25)
    per_nombre = models.CharField(max_length=45)
    per_apat = models.CharField(max_length=25)
    per_amat = models.CharField(max_length=25)
    per_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'persona'

