from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Caravan, CaravanImages, MessageForm as MessageObject, Calendar
from .forms import MessageForm
from django.core.mail import send_mail

def send_contact_email(name, email, message, datastart, dataend, phone):
    subject_to_me = f"Nowe zapytanie od {name}"
    message_to_me = f"Nowa wiadomość od: {name} ({email}), data startu: {datastart}, data końca: {dataend} \n {message} \n Numer telefonu: {phone}"
    send_mail(
        subject_to_me,
        message_to_me,
        email, 
        ['partneragd@vp.pl'], 
        fail_silently=False, 
    )

    # E-mail do użytkownika
    subject_to_user = "Potwierdzenie otrzymania zapytania"
    message_to_user = f"Dziękujemy za wysłanie zapytania, {name}!\n\nOtrzymaliśmy następującą wiadomość:\n{message}\nZakres dat: {datastart} - {dataend} \n\nSkontaktujemy się z Tobą wkrótce."
    send_mail(
        subject_to_user,  
        message_to_user,  
        'info@partnerkampery.pl',  
        [email],  
        fail_silently=False,  
    )

# Create your views here.
class HomePageView(TemplateView):
    template_name = "caravansApp/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['caravans'] = Caravan.objects.all()
        context['images'] = CaravanImages.objects.all()
        context['calendarDates'] = list(Calendar.objects.values())
        return context

    def post(self, request):
        form = MessageForm(request.POST or None)

        if form.is_valid():
            form = form.cleaned_data
            name = form["name"]
            email = form["email"]
            phone = form["phone"]
            datastart = form["datastart"]
            dataend = form["dataend"]
            message = form["message"]

            print("Name:", name)
            print("Email:", email)
            print("Phone:", phone)
            print("Start Date:", datastart)
            print("End Date:", dataend)
            print("Message:", message)

            datastart = form.get("datastart") or None
            dataend = form.get("dataend") or None

            new_message_Form = MessageObject(
                name=name,
                email=email,
                phone=phone,
                datastart=datastart,
                dataend=dataend,
                message=message
            )
            new_message_Form.save()

            send_contact_email(name, email, message, datastart, dataend, phone)

            return render(request=request, template_name=self.template_name, context={
                **self.get_context_data(),
                "success_message": "Wiadomość została wysłana pomyślnie, niedługo odpowiemy"
            })

        else:
            print("Form errors:", form.errors)
            return render(request=request, template_name=self.template_name, context={
                **self.get_context_data(),
                "warning_message": "Wiadomość nie została wysłana, spróbuj ponownie za chwilę bądź skontaktuj się z nami telefonicznie"
            })
        