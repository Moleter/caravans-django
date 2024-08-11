from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Caravan, CaravanImages, MessageForm as MessageObject, Calendar
from .forms import MessageForm
from django.core import serializers

# Create your views here.
class HomePageView(TemplateView):
    template_name = "caravansApp/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['caravans'] = Caravan.objects.all()
        context['images'] = CaravanImages.objects.all()
        context['calendarDates'] = list(Calendar.objects.values("startDate", "endDate"))
        return context

    def post(self, request):
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form = form.cleaned_data
            name = form["name"]
            email = form["email"]
            phone = form["phone"]
            message = form["message"]

            new_message_Form = MessageObject(name=name, email=email, phone=phone, message=message)
            new_message_Form.save()

            return render(request=request, template_name=self.template_name, context={
                **self.get_context_data(),
                "success_message": "Wiadomość została wysłana pomyślnie, niedługo odpowiemy"})

        else:
            return render(request=request, template_name=self.template_name, context={
                **self.get_context_data(),
                "warning_message": "Wiadomość nie została wysłana, spróbuj ponownie za chwilę bądź skontaktuj się z nami telefonicznie"})
        