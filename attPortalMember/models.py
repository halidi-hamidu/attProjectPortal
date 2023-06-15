from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.
class AttPortalMemberModel(models.Model):
    GENDER = (
        # ('', 'Select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    REGIONS=(
        ('Arusha', 'Arusha'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Dodoma', 'Dodoma'),
        ('Geita', 'Geita'),
        ('Iringa', 'Iringa'),
        ('Bukoba', 'Bukoba'),
        ('Mpanda', 'Mpanda'),
        ('Kigoma', 'Kigoma'),
        ('Moshi', 'Moshi'),
        ('Lindi', 'Lindi'),
        ('Babati', 'Babati'),
        ('Musoma', 'Musoma'),
        ('Mbeya', 'Mbeya'),
        ('Zanzibar City', 'Zanzibar City'),
        ('Morogoro', 'Morogoro'),
        ('Mtwara', 'Mtwara'),
        ('Mwanza', 'Mwanza'),
        ('Njombe', 'Njombe'),
        ('Wete', 'Wete'),
        ('Chake-Chake', 'Chake-Chake'),
        ('Kibaha', 'Kibaha'),
        ('Sumbawanga','Sumbawanga' ),
        ('Songea', 'Songea' ),
        ('Shinyanga', 'Shinyanga' ),
        ('Bariadi', 'Bariadi'),
        ('Singida', 'Singida'),
        ('Vwawa','Vwawa' ),
        ('Tabora', 'Tabora'),
        ('Tanga', 'Tanga'),
        ('Mkokotoni', 'Mkokotoni' ),
        ('Koani', 'Koani'),
    )
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    # upload_image= models.ImageField(upload_to='media')
    name = models.CharField(max_length=1000, null=True, blank=True)
    nationalID = models.CharField(max_length=1000, null=True, blank=True)
    age = models.CharField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=1000, null=True, blank=True,  choices=GENDER)
    occupation = models.CharField(max_length=1000, null=True, blank=True)
    region = models.CharField(max_length=1000, null=True, blank=True, choices=REGIONS )
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'attPortal Members'

    def __str__(self):
        return str(self.name)





