from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Bike(models.Model):

    bike_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    rating = models.FloatField(default=0.0, validators=[MaxValueValidator(10.0), MinValueValidator(0.0)])
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    bike_type =  models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('bikes:bike_edit', kwargs={'pk': self.pk})