from .models import Job
from django import forms

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


        widgets = {
            'posted_date' : forms.DateInput(attrs={'type' : 'date'}),
            'application_deadline' : forms.DateInput(attrs = {'type' : 'date'})
        }



