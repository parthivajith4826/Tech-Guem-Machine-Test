from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import login
from .models import Students,Course
from django.http import HttpResponse
from django.template.context_processors import request


# Create your views here.

def home(request):
    email = request.session.get("email")
    count = None
    user = None
    if email :
        user = get_object_or_404(Students, email=email)
        count = user.course.count()
    return render(request,'students/index.html',{"count":count,"user":user})

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'students/register.html',{"form":form})


def login(request):
    error = None
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        user = Students.objects.filter(name = name, email = email).first()
        if user :
            request.session["email"] = email
            return redirect("students:home")
        else :
            error = "User credential are wrong"
    return render(request,"students/login.html",{"error":error})


def courses(request):
    email = request.session.get("email")
    user = Students.objects.filter(email=email).first()
    if not user :
        return redirect("students:home")
    courses = Course.objects.all()
    return render(request,"students/courses.html",{"courses":courses})

def register_course(request,pk):
    email = request.session.get("email")
    user = Students.objects.filter(email=email).first()
    if not user :
        return redirect("students:home")
    
    email = request.session.get("email")
    user = get_object_or_404(Students, email=email)
    course = get_object_or_404(Course, id=pk)
    user.course.add(course)
    user.save()
    return redirect("students:courses")


def logout(request):
    email = request.session.get("email")
    user = Students.objects.filter(email=email).first()
    if not user :
        return redirect("students:home")
    request.session.flush()
    return redirect("students:home")
