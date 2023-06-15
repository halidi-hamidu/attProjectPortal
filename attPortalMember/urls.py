from django.urls import path, include
from . import views 


app_name = 'attPortalMember'
urlpatterns = [
  
      path('', views.attPortalMemberPage, name='attPortalMemberPage'),
]

