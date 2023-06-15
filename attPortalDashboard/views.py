from django.shortcuts import render
from attPortalMember.forms import AttPortalMemberModelForm
# Create your views here.
def attPortalDashboardPage(request):
    form = AttPortalMemberModelForm()
    template_name = 'attPortalDashboard/attPortalDashboardPage.html'
    context = {
        'form':form
    }

    return render (request, template_name, context)