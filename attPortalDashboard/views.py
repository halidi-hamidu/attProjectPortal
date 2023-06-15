from django.shortcuts import render, redirect
from attPortalMember.forms import AttPortalMemberModelForm
from django.contrib import messages
from attPortalMember.models import AttPortalMemberModel
# Create your views here.
def attPortalDashboardPage(request):
    try:
        if request.method == "POST":
            form = AttPortalMemberModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, " Member added successful")
                return redirect("attPortalDashboard:attPortalDashboardPage")
    except:
        return redirect("attPortalDashboard:attPortalDashboardPage")
    get_all_member= AttPortalMemberModel.objects.all().order_by('-created_at')
    count_all_member= AttPortalMemberModel.objects.all().count
    form = AttPortalMemberModelForm()
    template_name = 'attPortalDashboard/attPortalDashboardPage.html'
    context = {
        'form':form,
        'get_all_member':get_all_member,
        'count_all_member':count_all_member
    }

    return render (request, template_name, context)

    