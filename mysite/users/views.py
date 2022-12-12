from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.views.generic import CreateView

# Create your views here.
class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = NewUserForm

    def form_valid(self, form, request):
        form.save()
        return render(request,'login.html')