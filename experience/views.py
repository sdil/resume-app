from django.shortcuts import render, redirect, get_object_or_404
from .models import Experience
from .forms import ExperienceForm
from django.contrib import messages


def main(request):
    """
    Show experience list
    """
    experiences = Experience.objects.all().order_by("start_date")
    return render(
        request, "experience/experience_list.html", {"experiences": experiences},
    )


def dashboard(request):
    """
    Show experience list with update and delete buttons
    """
    experiences = Experience.objects.all().order_by("start_date")
    return render(request, "experience/dashboard.html", {"experiences": experiences},)


def details(request, pk):
    """
    Show experience details
    """
    experience = get_object_or_404(Experience, id=pk)
    return render(
        request, "experience/experience_details.html", {"experience": experience},
    )


def create(request):
    """
    GET: Show experience create form
    POST: Create experience instance
    """
    if request.method == "GET":
        form = ExperienceForm()
        return render(request, "experience/experience_form.html", {"form": form,},)
    elif request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "The form is invalid")
            return render(request, "experience/experience_form.html", {"form": form,},)

    return redirect("dashboard")


def update(request, pk):
    """
    GET: Show experience update form
    POST: Update experience instance
    """
    experience = get_object_or_404(Experience, id=pk)

    if request.method == "GET":
        form = ExperienceForm(instance=experience)
        return render(request, "experience/experience_form.html", {"form": form,},)
    elif request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "The form is invalid")
            return render(request, "experience/experience_form.html", {"form": form,},)

    return redirect("dashboard")


def delete(request, pk):
    """
    Delete experience instance
    """
    experience = get_object_or_404(Experience, id=pk)
    experience.delete()
    return redirect("dashboard")
