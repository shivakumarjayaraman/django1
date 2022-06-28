from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse

#def homePageView(r) :
#    return HttpResponse("Hello World")

class HomePageView(TemplateView) :
    template_name = "home.html"

class AboutPageView(TemplateView) :
    template_name = "about.html"
