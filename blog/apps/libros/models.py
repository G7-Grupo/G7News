from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length = 80)
    apellido = models.CharField(max_length = 80)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'


class Libro(models.Model):
    titulo = models.CharField(max_length = 200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.titulo

