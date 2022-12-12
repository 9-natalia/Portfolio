from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class MyappView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    extra_context = {"people": Person.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["people"] = Person.objects.all()
        return context

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def resume(request):
    return render(request,'resume.html')

@login_required
def portfolio(request):
    return render(request,'portfolio.html')

@login_required
def login(request):
    return render(request,'login.html')

@login_required
def contact(request):
    return render(request,'contact.html')