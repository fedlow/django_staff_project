from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin # К8
from .models import Employee

class HomePageView(ListView):
    model = Employee
    template_name = 'staff/home.html'
    context_object_name = 'employees'

class EmployeeListView(ListView):
    model = Employee
    template_name = 'staff/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(LoginRequiredMixin, DetailView): 
    model = Employee
    template_name = 'staff/employee_detail.html'
    context_object_name = 'employee'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all() 
        return context