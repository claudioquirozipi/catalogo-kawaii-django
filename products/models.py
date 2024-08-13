from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='img/products', null=True, blank=True)
    
    def __str__(self):
        return self.name