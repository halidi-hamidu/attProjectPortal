
from django.urls import path, include
from . import views 

app_name = 'attPortalDashboard'

urlpatterns = [
  
      path('', views.attPortalDashboardPage, name='attPortalDashboardPage'),
]

