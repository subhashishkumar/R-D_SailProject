from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "welcome.html"

class MemberPageView(TemplateView):
    template_name = 'member.html'