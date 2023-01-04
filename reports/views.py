from django.shortcuts import render
from .models import Report, ReportKind

# Create your views here.


def all_reports(request):
    context = {}
    reports = Report.objects.all()
    context["reports"] = reports
    return render(request, 'all_reports.html', context=context)


def show_report(request, report_id):
    context = {}
    report = Report.objects.get(pk=report_id)
    context["report"] = report
    return render(request, 'show_report.html', context=context)

