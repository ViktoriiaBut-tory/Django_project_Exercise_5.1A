from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "pages/home.html")


def courses(request):
    return render(request, "pages/courses.html")


def contact(request):
    return render(request, "pages/contact.html")
