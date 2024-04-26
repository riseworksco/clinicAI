import io

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from reportlab.pdfgen import canvas

from sheetRAS.forms import RasForm


class RASView(FormView):
    template_name = "assessment/test1.html"
    form_class = RasForm
    success_url = reverse_lazy("assessment:success")

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
