from django.shortcuts import render

from assessment.forms import StompForm


# Create your views here.
def index(request):
    form = StompForm()
    # rendered_form = form.render("form_snippet.html")
    context = {'form': form}
    return render(request, 'assessment/stomp.html', context)
