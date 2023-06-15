from dataclasses import field, fields
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
class AttPortalMemberModelForm(ModelForm):
  class Meta:
    model =AttPortalMemberModel
    fields = '__all__'
    exclude =[
      'created_at',
      'updated_at'
    ]
    