from django.db import models

class Experience(models.Model):
    titile = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=100, null=False)
    start_year = models.DateTimeField()
    end_year = models.DateTimeField()