from django.db import models

# Create your models here.

class Imagem(models.Model):
    imagem = models.CharField(max_length=32)
    clusters = models.IntegerField()
    img = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.imagem