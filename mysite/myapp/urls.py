from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('resume',views.resume, name='resume'),
    path('contact',views.contact, name='contact'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('login',views.login, name='login'),
    re_path(r'portfolio/add', views.addProject, name='add')
]
 