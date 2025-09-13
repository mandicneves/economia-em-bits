from django.shortcuts import render, get_object_or_404
from .models import Project
from .utils import generate_forecast_plot

# Create your views here.
def portfolio_list(request, *args, **kwargs):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio_list.html", {})

def portfolio_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    forecast_plot = generate_forecast_plot() if project.slug == "modelo-de-previsao-de-series-temporais" else None
    return render(request, 'portfolio/portfolio_detail.html', {
        'project': project,
        'forecast_plot': forecast_plot
    })