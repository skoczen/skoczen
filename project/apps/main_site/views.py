from annoying.decorators import render_to
from main_site.models import all_pages

@render_to("main_site/home.html")
def home(request):
    pages = all_pages
    return locals()


@render_to("main_site/threaded.html")
def threaded(request):
    return locals()
