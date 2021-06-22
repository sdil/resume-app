from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Experience
from django.views.generic import ListView
from .forms import ExperienceForm


class ExperienceListView(ListView):
    model = Experience


class ExperienceCreateView(CreateView):
    model = Experience
    form_class = ExperienceForm
    success_url = reverse_lazy("experience-list")


class ExperienceUpdateView(UpdateView):
    model = Experience
    fields = ["title"]


class ExperienceDeleteView(DeleteView):
    model = Experience
    success_url = reverse_lazy("experience-list")
