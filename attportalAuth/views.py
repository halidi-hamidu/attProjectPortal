from django.shortcuts import render

# Create your views here.
def attportalAuth(request):
    template_name = 'attportalAuth/attportalAuth.html'
    context ={

    }

    return render (request, template_name, context)