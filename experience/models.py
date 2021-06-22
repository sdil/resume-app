from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
