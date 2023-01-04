from django.urls import path
from . import views

urlpatterns = [
    path('all_reports', views.all_reports, name='all_reports'),

]
