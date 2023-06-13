
from django.urls import path, include
from . import views 


app_name= 'attportalAuth'
urlpatterns = [
  
      path('', views.attportalAuth, name='attportalAuth'),
]
