from django.urls import path
from . import views

urlpatterns = [
    path('all_reports', views.all_reports, name='all_reports'),
    path('show_report/<report_id>', views.show_report, name='show_report'),

]
