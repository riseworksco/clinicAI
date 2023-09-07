from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"header": "Chat"}
    return render(request, "chat/index.html", context)
