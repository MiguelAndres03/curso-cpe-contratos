from django.db import models

# Create your models here.


class Persona(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombre


class Supervisor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisors"

    def __str__(self):
        return self.nombre


class Contratista(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contratista"
        verbose_name_plural = "Contratistas"

    def __str__(self):
        return self.nombre
