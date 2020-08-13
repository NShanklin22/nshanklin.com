from django.shortcuts import render
import os
import sys
sys.path.append(os.path.realpath('..'))
from scripts import test

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def learning(request):
    return render(request,'learning.html')

def blog(request):
    return render(request,'blog.html')

def project_one(request):
    return render(request,'projects/project_one.html')

def project_two(request):
    return render(request,'projects/project_two.html')
