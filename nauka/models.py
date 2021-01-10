from django.db import models
from django.urls import reverse

# Create your models here.
class Prod(models.Model):
    prodName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    # image = models.FileField(blank=True,null=True,upload_to='images')
    def get_absolute_url(self):
        # return reverse('detail-product',kwargs={'pk': self.pk})
        return reverse('main')
    def __str__(self):
        return self.prodName
