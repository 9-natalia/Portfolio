from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, Project
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import MyProjectForm
# Create your views here.

def home(request):
    return render(request,'home.html')

# @login_required
def about(request):
    return render(request,'about.html')

# @login_required
def resume(request):
    return render(request,'resume.html')

# @login_required
def portfolio(request):
    task = Project.objects.all()
    context = { 'task': task }
    return render(request, "portfolio.html", context)

# @login_required
def login(request):
    return render(request,'login.html')

# @login_required
def contact(request):
    return render(request,'contact.html')

@login_required
def addProject(request):
    if request.method == 'POST':
        form = MyProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = MyProjectForm()
    return render(request, 'add.html', {'form': form})