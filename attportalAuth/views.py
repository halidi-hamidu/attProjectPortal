from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def attportalAuth(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successful login")
            return redirect('attPortalDashboard:attPortalDashboardPage')
        else:
            pass
            # Return an 'invalid login' error message.
        
    else:
        form = AuthenticationForm()
        template_name = 'attportalAuth/attPortalAuth.html'
        context ={
            'form':form
        }

        return render (request, template_name, context)