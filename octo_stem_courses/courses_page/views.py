# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def courses_page(request):
    template = loader.get_template('courses_home.html')
    return HttpResponse(template.render())
