from .models import Job, ContactMessage
from django import forms

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


        widgets = {
            'posted_date' : forms.DateInput(attrs={'type' : 'date'}),
            'application_deadline' : forms.DateInput(attrs = {'type' : 'date'})
        }


from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message']

