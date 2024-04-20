import io
import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from reportlab.pdfgen import canvas

from assessment.forms import (AAQ2Form, AT4Form, CAM1Form, GAD7Form,
                              NeurologicScreeningEvaluationForm, PHQ9Form,
                              PrePostForm,
                              PsychoemotionalScreeningEvaluationForm, RASForm,
                              StompForm)
from assessment.pdf_generator import render_pdf

#from sheet4AT.forms import ATForm




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




class AT4View(LoginRequiredMixin, FormView):
    template_name = 'assessment/AT4.html'
    form_class = AT4Form
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        logging.info(12)
        form.send()
        return super().form_valid(form)


class AAQ2View(FormView):
    template_name = 'assessment/AAQII.html'  # 确保模板路径正确
    form_class = AAQ2Form
    success_url = reverse_lazy('assessment:success')  # 更新这里以匹配您的URL配置

    def get_context_data(self, **kwargs):
        # 调用基类方法获取上下文
        context = super().get_context_data(**kwargs)

        # 如果表单存在于上下文中，添加问题字段到上下文
        if 'form' in context:
            form = context['form']
            # 创建包含所有问题字段的列表
            context['questions'] = [form[f'question{i}'] for i in range(1, 8)]

        return context

    def form_valid(self, form):
        # 这里可以添加您的表单处理逻辑
        # 例如，您可以在这里计算总分并保存结果，或者执行其他操作
        total_score = form.calculate_total_score()

        # 可以根据需要添加额外逻辑
        # ...
        form.send()
        return super().form_valid(form)


class CAM1View(FormView):
    template_name = 'assessment/CAM.html'
    form_class = CAM1Form
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


class GAD7View(FormView):
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


class PHQ9View(FormView):
    template_name = 'assessment/PHQ-9.html'
    form_class = PHQ9Form
    success_url = reverse_lazy('assessment:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' in context:
            # Manually add each question field to the context
            context['questions'] = [context['form'][f'question{i}'] for i in range(1, 11)]
        return context

    def form_valid(self, form):
        form .send()  # Send your email
        return super().form_valid(form)  # Redirect to success_url



class RASView(FormView):
    template_name = 'assessment/test1.html'
    form_class = RASForm
    success_url = reverse_lazy('assessment:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


