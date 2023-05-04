from dataclasses import field
from django.forms import ModelForm 
from django import forms 
from .models import user_data
   
# creating a form 
class InputForm(ModelForm):
    name = forms.CharField(max_length = 50)
    roll_no = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    class Meta:
        model = user_data
        fields = ['name', 'roll_no']