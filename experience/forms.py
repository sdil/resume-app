import logging
from django import forms
from .models import Experience


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = "__all__"