from __future__ import unicode_literals

from django.db import models

class Bloque(models.Model):
    id_bloq = models.AutoField(primary_key=True)
    bloq_tiempo = models.FloatField(unique=True)

    def __str__(self):
        return str(self.bloq_tiempo)

    class Meta:
        managed = False
        db_table = 'bloque'
        
class Usuario(models.Model):
    id_us = models.AutoField(primary_key=True)
    id_bloq = models.ForeignKey(Bloque, models.DO_NOTHING, db_column='id_bloq')
    us_nombre = models.CharField(max_length=45)
    us_apat = models.CharField(max_length=25)
    us_amat = models.CharField(max_length=25)
    us_slug = models.CharField(unique=True, max_length=10)
    us_user = models.CharField(unique=True, max_length=15)
    us_pass = models.CharField(max_length=35)

    def __unicode__(self):
        return self.us_nombre + " " + self.us_apat + " " + self.us_amat

    class Meta:
        managed = False
        db_table = 'usuario'

class Periodo(models.Model):
    id_prd = models.AutoField(primary_key=True)
    id_us = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_us')
    prd_inicio = models.TimeField()
    prd_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'periodo'


