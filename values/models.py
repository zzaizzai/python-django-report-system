from django.db import models
from reports.models import Report

# Create your models here.


class ValueKind(models.Model):
    method = models.CharField('method', max_length=255)
    unit = models.CharField('unit', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    explain = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.method


class Value(models.Model):
    kind = models.ForeignKey(ValueKind, on_delete=models.CASCADE)
    parent_report = models.ForeignKey(Report,null=True, default=None, on_delete=models.SET_NULL)
    value = models.FloatField('value', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
