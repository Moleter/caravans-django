from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Caravan(models.Model):
    name = models.CharField(_("Nazwa"), max_length=255)
    description = models.TextField(_("Opis"))
    seating = models.CharField(_("Liczba miejsc"), max_length=63)
    transmission = models.CharField(_("Skrzynia biegów"), max_length=63)
    year_of_production = models.IntegerField(_("Rok produkcji"))
    engine = models.CharField(_("Silnik"), max_length=63, default=None)
    horse_power = models.IntegerField(_("Konie Mechaniczne"), default=None)

    def __str__(self) -> str:
        return self.name

class CaravanImages(models.Model):
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    image = models.ImageField(_("Zdjęcia"), upload_to="images")

    def __str__(self) -> str:
        return f"{self.caravan} {self.image}"

class Calendar(models.Model):
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    startDate = models.DateField(_("Data początkowa"))
    endDate = models.DateField(_("Data końcowa"))

    def __str__(self) -> str:
        return f"Rezerwacja od {self.startDate} do {self.endDate}"

class MessageForm(models.Model):
    name = models.CharField(_("Imię"), max_length=254)
    email = models.CharField(max_length=254)
    phone = models.CharField(_("Numer telefonu"), max_length=20)
    message = models.CharField(_("Wiadomość"), max_length=511)

    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"