# forms.py 
from django import forms 
from .models import *
from django.db import models
  
class UserForm(forms.ModelForm): 
  
    class Meta: 
        model = Use 
        fields = ['name', 'x_ray_img'] 

