from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def portfolio_list(request, *args, **kwargs):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio_list.html", {})

def portfolio_detail(request, slug, *args, **kwargs):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/portfolio_detail.html", {})