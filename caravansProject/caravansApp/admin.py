from django.contrib import admin
from .models import Calendar, Caravan, CaravanImages, MessageForm

# Register your models here.
admin.site.register(CaravanImages)
admin.site.register(Caravan)
admin.site.register(Calendar)
admin.site.register(MessageForm)
