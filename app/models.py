from django.db import models


class ArchivoMulticloud(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='multicloud/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
