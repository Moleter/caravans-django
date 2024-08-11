from django.db import models
from django.contrib.postgres.fields import DateRangeField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Caravan(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))

    def __str__(self) -> str:
        return self.name

class CaravanImages(models.Model):
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to="images")

    def __str__(self) -> str:
        return f"{self.caravan} {self.image}"

class Calendar(models.Model):
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    startDate = models.DateField(_("Data początkowa"))
    endDate = models.DateField(_("Data końcowa"))

    def __str__(self) -> str:
        return f"Rezerwacja od {self.startDate} do {self.endDate}"

class MessageForm(models.Model):
    name = models.CharField(_("Name"), max_length=254)
    email = models.CharField(max_length=254)
    phone = models.CharField(_("Phone"), max_length=20)
    message = models.CharField(_("Message"), max_length=511)

    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"