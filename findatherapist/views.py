from collections import defaultdict

from django.shortcuts import render


# Create your views here.
def index(request):
    context = defaultdict()
    context["header"] = "Find A Therapist"
    return render(request, "findatherapist/index.html", context)
