from django.shortcuts import render, redirect
from attPortalMember.forms import AttPortalMemberModelForm
from django.contrib import messages
# Create your views here.
def attPortalDashboardPage(request):
    if request.method == "POST":
        form = AttPortalMemberModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Member added successful")
            return redirect("attPortalDashboard:attPortalDashboardPage")
    form = AttPortalMemberModelForm()
    template_name = 'attPortalDashboard/attPortalDashboardPage.html'
    context = {
        'form':form
    }

    return render (request, template_name, context)