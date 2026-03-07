from django.shortcuts import render
from students.models import Students,Course
from rest_framework import generics
from .serializers import StudentSerializer, CourseSerializer


class Students(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
    
#     lookup_field = 'pk'  
    
class Courses(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    lookup_field = 'pk' 