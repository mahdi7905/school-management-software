from django import forms
from django.forms import ModelForm
from .models import *


class applicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['date_created']