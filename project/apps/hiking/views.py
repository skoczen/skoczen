from annoying.decorators import render_to

from hiking.models import Hike


@render_to("hiking/home.html")
def home(request):
    hike = Hike.objects.order_by("date")
    if hike.count() > 0:
        hike = hike[0]
    return locals()
