from django.urls import path

from .views import (
    main,
    dashboard,
    create,
    details,
    update,
    delete,
)

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("", main, name="experience-list"),
    path("add/", create, name="experience-add"),
    path("details/<int:pk>/", details, name="experience-details"),
    path("<int:pk>/", update, name="experience-update"),
    path("<int:pk>/delete/", delete, name="experience-delete"),
]
