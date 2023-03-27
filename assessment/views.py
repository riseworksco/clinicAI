from django.shortcuts import render

from assessment.forms import StompForm, NeurologicScreeningEvaluationForm, PrePostForm


# Create your views here.
def stomp(request):
    form = StompForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
        Please indicate your basic preference for each of the following genres using the scale provided.
1-----------------2-----------------3-----------------4-----------------5-----------------6-----------------7
Dislike Dislike Dislike a Neither like Like a Like Like
    """
    context = {
        'form': form,
        'header': 'STOMP-Revised',
        'description': description,
        'therapist': request.user.username}
    return render(request, 'assessment/stomp.html', context)


def neurologic_screening_evaluation(request):
    form = NeurologicScreeningEvaluationForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
Description for the form
        """
    context = {
        'form': form,
        'header': 'Neurologic Screening/Evaluation',
        'description': description,
        'therapist': request.user.username
    }
    return render(request, 'assessment/neurologic_screening_evaluation.html', context)


def pre_post_form(request):
    form = PrePostForm()
    # rendered_form = form.render("form_snippet.html")
    description = """
Description for the form
        """
    context = {'form': form, 'header': 'Pre/Post Tests', 'description': description}
    return render(request, 'assessment/pre_post_form.html', context)
