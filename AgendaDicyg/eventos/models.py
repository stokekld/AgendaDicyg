from __future__ import unicode_literals

from django.db import models

from usuarios.models import Usuario
from personas.models import Persona

class Evento(models.Model):
    id_event = models.AutoField(primary_key=True)
    id_us = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_us')
    id_per = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_per')
    event_inicio = models.DateTimeField()
    event_fin = models.DateTimeField()
    event_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'

