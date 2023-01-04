from django.db import models

# Create your models here.


class ReportKind(models.Model):
    method = models.CharField('method', max_length=255)
    unit = models.CharField('unit', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    explain = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.method


class Report(models.Model):
    kind = models.ForeignKey(ReportKind, null=True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
