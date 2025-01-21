from django import forms

class MessageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    dateStart = forms.DateField()
    dateEnd = forms.DateField()
    phone = forms.CharField()
    message = forms.CharField()

    
