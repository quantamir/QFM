from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from dashboard.models import Employee
from .forms import EmployeeForm


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    paginate_by = 20
    ordering = ["-id"]


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "پرسنل با موفقیت اضافه شد.")
        return response


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "اطلاعات پرسنل با موفقیت ویرایش شد.")
        return response


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employee_list")

    def form_valid(self, form):
        messages.success(self.request, "پرسنل با موفقیت حذف شد.")
        return super().form_valid(form)