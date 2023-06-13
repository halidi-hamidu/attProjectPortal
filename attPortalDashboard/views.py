from django.shortcuts import render

# Create your views here.
def attPortalDashboardPage(request):
    template_name = 'attPortalDashboard/attPortalDashboardPage.html'
    context = {

    }

    return render (request, template_name, context)