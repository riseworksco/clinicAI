from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render

from .forms import GAD7Form


class GADView(FormView):
    template_name = 'assessment/GAD-7.html'
    form_class = GAD7Form
    success_url = reverse_lazy('assessment:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' in context:
            form = context['form']
            context['questions'] = [form[f'question{i}'] for i in range(1, 9)]  # Include question8 if it exists
        return context

    def form_valid(self, form):
        total_score = form.calculate_total_score()
        anxiety_level = form.get_anxiety_level(total_score)
        # You might want to do something with total_score and anxiety_level here,
        # like saving them to the database.

        form.send()  # Send your email

        # Optionally, store values in session if you want to use them after redirect
        self.request.session['total_score'] = total_score
        self.request.session['anxiety_level'] = anxiety_level

        return super().form_valid(form)  # Redirect to success_url

    def form_invalid(self, form):
        return super().form_invalid(form)
