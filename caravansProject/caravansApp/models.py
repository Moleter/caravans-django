from django.db import models
from django.contrib.postgres.fields import DateRangeField

# Create your models here.
class Caravan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class CaravanImages(models.Model):
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return f"{self.caravan} {self.image}"

class Calendar(models.Model):
    date = DateRangeField()