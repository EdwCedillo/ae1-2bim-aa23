from django.db import models

# Create your models here.
class EntidadProveedor(models.Model):
    ruc = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=30)
    cupo = models.IntegerField() #cantidad max de cupo de credito
    tiempo_credito = models.IntegerField() #tiempo en dias de credito
    nombre_comercial = models.CharField(max_length=100)

    def __str__(self):
        return """RUC: %s - Rason Social: %s \n
                Cupo Maximo: %d\n
                Tiempo de Credito: %d\n
                Nombre Comercial: %s""" % (self.ruc,
                self.razon_social,
                self.cupo,
                self.tiempo_credito,
                self.nombre_comercial)
