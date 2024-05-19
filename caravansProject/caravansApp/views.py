from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Caravan, CaravanImages

# Create your views here.
class HomePageView(TemplateView):
    template_name = "caravansApp/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['caravans'] = Caravan.objects.all()
        context['images'] = CaravanImages.objects.all()
        return context

        