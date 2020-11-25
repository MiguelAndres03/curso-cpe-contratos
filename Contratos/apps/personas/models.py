from django.db import models

# Create your models here.


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=45)
    apellido1 = models.CharField(max_length=45)
    apellido2 = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre


class Supervisor(models.Model):
    id = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisors"

    def __str__(self):
        return self.id


class Contratista(models.Model):
    id = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Contratista"
        verbose_name_plural = "Contratistas"

    def __str__(self):
        return self.id
