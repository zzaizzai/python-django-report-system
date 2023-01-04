from django.shortcuts import render

# Create your views here.


def all_reports(request):
    return render(request, 'all_reports.html', {})
