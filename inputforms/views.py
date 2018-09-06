from login.models import *
from inputforms.forms import *
from inputforms.models import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def get_unit_name(self):
    if self.request.user.is_authenticated:
        current_user = self.request.user.username
        uname = User.objects.get(username=current_user)
        unit = uname.profile.unit
        return unit


class AccdView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AllAccident
    form_class = AccdForm
    login_url = '/users/login_user/'
    # check url name for the view
    success_url = reverse_lazy('AccdForm')
    success_message = 'Success! Accident Data Submitted'

    def form_valid(self, form):
        emp_details = form.save(commit=False)
        emp_details.unit_name = get_unit_name(self)
        emp_details.save()
        return SuccessMessageMixin.form_valid(self, form)


class ManhoursView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Manhours
    form_class = ManhoursForm
    login_url = '/users/login_user/'
    success_url = reverse_lazy('ManhoursForm')
    success_message = 'Success! Data Submitted'

    def form_valid(self, form):
        manhours = form.save(commit=False)
        manhours.unit_name = get_unit_name(self)
        manhours.save()
        return SuccessMessageMixin.form_valid(self, form)
