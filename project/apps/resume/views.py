from collections import OrderedDict
from annoying.decorators import render_to

@render_to("resume/home.html")
def home(request):

    skill_values = OrderedDict([
        ("UX", 7),
        ("UI", 6),
        ("Design", 5),
        ("Front-end", 9),
        ("Back-end", 8),
        ("Devops", 6),
        ("DBA", 4),
        ("Server-admin", 4),
    ])
    return locals()
