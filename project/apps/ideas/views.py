from annoying.decorators import render_to

from ideas.models import Idea


@render_to("ideas/home.html")
def home(request):
    idea = Idea.objects.order_by("-date")
    if idea.count() > 0:
        idea = idea[0]
    return locals()
