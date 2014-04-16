from annoying.decorators import render_to
from main_site.models import Project


@render_to("main_site/home.html")
def home(request):
    projects = Project.objects.all().order_by("-date_started")
    return locals()


@render_to("main_site/uptime.html")
def uptime(request):
    return locals()


@render_to("main_site/threaded.html")
def threaded(request):
    return locals()


@render_to("main_site/new_years.html")
def new_year(request):
    return locals()