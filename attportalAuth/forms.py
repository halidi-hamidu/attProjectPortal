from dataclasses import field, fields
from pyexpat import model
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class ProductTableForm(ModelForm):
  class Meta:
    model =AuthenticationForm
    fields = '__all__'
    