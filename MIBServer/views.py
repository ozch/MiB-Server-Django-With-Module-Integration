from django.shortcuts import render
def Dashboard(request):
    context = {
        'page_title' : "- Dashboard"
    }
    return render(request=request,template_name='dashboard.html',context=context)