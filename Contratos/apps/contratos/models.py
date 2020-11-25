from django.db import models

# Create your models here.


class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    objeto = models.TextField(max_length=140)
    valorTotal = models.IntegerField()
    fechaSubscripcion = models.DateTimeField(auto_now = True)
    fechaTerminación = models.DateTimeField(auto_now = True)
    estado = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return self.id


class Seguimiento(models.Model):
    id = models.AutoField(primary_key=True)
    idcontrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    entregado = models.BooleanField()

    class Meta:
        verbose_name = "Seguimiento"
        verbose_name_plural = "Seguimientos"

    def __str__(self):
        return self.id


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=140)
    valorUnidad = models.IntegerField()
    fechaEntrega = models.DateTimeField(auto_now = True)
    fechaVencimiento = models.DateTimeField(auto_now = True)
    activo = models.BooleanField()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
