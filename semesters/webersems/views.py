from django.shortcuts import render,redirect
import requests
from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
from .models import Link, Courses
from .forms import FormSchool, FormSemester
from django.http import HttpResponseRedirect
from .serializers import *



def index(request):
    form = FormSchool(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'index.html', {'form': form})

def scrape(request):
    if request.method == "POST":
        site=request.POST.get('site', '')

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    data = Link.objects.all()

    return render(request, 'result.html', {'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'result.html')

def sems(request):
    form = FormSemester(request.POST or None)
    semester = Semester.objects.all().values()
    serializer = CourseSerializer(Courses, many=True)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'semesters.html', {'form': form, 'semester': semester})

def classes(request):
    courses = Courses.objects.all().values()
    form = FormSchool(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'classes.html', {'form': form, 'courses': courses})