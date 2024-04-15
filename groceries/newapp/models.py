from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    quant = models.IntegerField()

    def __str__(self):
        return self.title