from django.shortcuts import render
from . models import Students


def home(request):
    return render(request,'app/home.html')



def students(request):
    students = Students.objects.all()
    context = {
        "students" : students
    }
    return render(request, 'extra/students.html', context)
