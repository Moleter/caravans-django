from django import forms

class MessageForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    datastart = forms.DateField(required=False) 
    dataend = forms.DateField(required=False)    
    phone = forms.CharField()
    message = forms.CharField()