from django.urls import path

from .views import (
    ExperienceListView,
    ExperienceCreateView,
    ExperienceUpdateView,
    ExperienceDeleteView,
)

urlpatterns = [
    path("", ExperienceListView.as_view(), name="experience-list"),
    path("add/", ExperienceCreateView.as_view(), name="experience-add"),
    path("<int:pk>/", ExperienceUpdateView.as_view(), name="experience-update"),
    path("<int:pk>/delete/", ExperienceDeleteView.as_view(), name="experience-delete"),
]
