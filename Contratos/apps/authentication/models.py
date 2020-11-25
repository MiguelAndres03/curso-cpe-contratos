from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=20)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.id
