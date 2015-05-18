from django.utils.timezone import now
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Invervento(models.Model):
    class Meta:
        abstract = True

    planned = "PI"
    done = "SV"

    status_choices = (
        (planned, "Pianificato"),
        (done, "Svolto")
    )

    status = models.CharField(choices=status_choices, blank=False, null=False, max_length=2,
                              verbose_name="Stato dell'intervento")
    degrado = models.IntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    nome = models.CharField(blank=False, null=False, max_length=250,
                            help_text="Nome dell'intervento")
    partecipanti = models.IntegerField(blank=True, null=True,
                                       help_text="Numero di persone coinvolte")
    date = models.DateField(blank=False, null=True, verbose_name="Data")
    aggiunto = models.DateField(blank=False, null=False, default=now())
    descrizione = models.CharField(blank=True, null=True, max_length=250,
                                   help_text="Descrizione dell'intervento")

    def __unicode__(self):
        return self.nome


class PuntoIntervento(Invervento):

    class Meta:
        verbose_name_plural = "Punto intervento"

    point = models.PointField(srid=4326, spatial_index=True, blank=False, null=False,
                              verbose_name="Punto invervento")


class PercorsoIntervento(Invervento):

    class Meta:
        verbose_name_plural = "Percorso intervento"

    line = models.MultiLineStringField(null=True, blank=True,
                                       verbose_name="Percorso intervento")
