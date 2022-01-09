from django.shortcuts import render
from .models import Instructor
# Create your views here.

def instructor(request):
    instructor_list=Instructor.objects.all()
    return render(request,'instructors.html',context={'instructor_list':instructor_list})