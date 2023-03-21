from django.shortcuts import render


# Create your views here.
def display_profile(request):
    return render(request, "registration/profile.html")
