from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from .forms import AAQIIForm  # 确保这个路径正确对应到您的表单类


class AAQIIView(FormView):
    template_name = "assessment/AAQII.html"  # 确保模板路径正确
    form_class = AAQIIForm
    success_url = reverse_lazy("assessment:success")  # 更新这里以匹配您的URL配置

    def get_context_data(self, **kwargs):
        # 调用基类方法获取上下文
        context = super().get_context_data(**kwargs)

        # 如果表单存在于上下文中，添加问题字段到上下文
        if "form" in context:
            form = context["form"]
            # 创建包含所有问题字段的列表
            context["questions"] = [form[f"question{i}"] for i in range(1, 8)]

        return context

    def form_valid(self, form):
        # 这里可以添加您的表单处理逻辑
        # 例如，您可以在这里计算总分并保存结果，或者执行其他操作
        total_score = form.calculate_total_score()

        # 可以根据需要添加额外逻辑
        # ...
        form.send()
        return super().form_valid(form)


# 如果您还有其他视图类，可以继续在此文件中添加它们
