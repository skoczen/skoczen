from annoying.decorators import render_to

@render_to("main_site/home.html")
def home(request):
    return locals()
