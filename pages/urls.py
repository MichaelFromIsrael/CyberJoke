from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import HomePageView, SignUp
from django.contrib import admin

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    
    
]