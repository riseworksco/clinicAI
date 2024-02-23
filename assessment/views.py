import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from assessment.forms import StompForm, NeurologicScreeningEvaluationForm, PrePostForm, \
    PsychoemotionalScreeningEvaluationForm

from assessment.pdf_generator import render_pdf



@login_required(login_url='/accounts/login/')
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


# @login_required(login_url='/accounts/login/')
# def pre_post_form(request):
#     form = PrePostForm()
#     # rendered_form = form.render("form_snippet.html")
#     description = """
# Description for the form
#         """
#     context = {'form': form, 'header': 'Pre/Post Tests', 'description': description}
#     return render(request, 'assessment/pre_post_form.html', context)


# Stomp Form related views
class StompView(LoginRequiredMixin, FormView):
    template_name = 'assessment/stomp.html'
    form_class = StompForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class StompSuccessView(TemplateView):
    template_name = 'email/success.html'


# Pre Post Form related view
class PrePostView(LoginRequiredMixin, FormView):
    template_name = 'assessment/pre_post_form.html'
    form_class = PrePostForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class PrePostSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'email/success.html'


class PsychoemotionalScreeningEvaluationView(LoginRequiredMixin, FormView):
    template_name = 'assessment/Psychoemotional_Screening_Evaluation.html'
    form_class = PsychoemotionalScreeningEvaluationForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


def index(request):
    prePostForm = PrePostForm()
    neurologicScreeningEvaluationForm = NeurologicScreeningEvaluationForm()
    context = {
        'prePostForm': prePostForm,
        'neurologicScreeningEvaluationForm': neurologicScreeningEvaluationForm,
        'header': 'Assessment',
        'therapist': request.user.username}
    return render(request, "assessment/index.html", context)


class NeurologicScreeningEvaluationView(LoginRequiredMixin, FormView):
    template_name = 'assessment/neurologic_screening_evaluation.html'
    form_class = NeurologicScreeningEvaluationForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class NeurologicScreeningEvaluationSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'email/success.html'


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')