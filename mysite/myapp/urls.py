from django.urls import path
from . import views

urlpatterns = [
    path('',views.MyappView.as_view(), name='home'),
    path('about',views.about, name='about'),
    path('resume',views.resume, name='resume'),
    path('contact',views.contact, name='contact'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('login',views.login, name='login'),
]