from django.urls import path,include
from . import views


urlpatterns = [
    path('students/',views.Students.as_view()),
    # path('students/<int:pk>/',views.StudentDetail.as_view()),
    path('courses/',views.Courses.as_view()),
    path('course/<int:pk>/',views.CourseDetail.as_view()),
]
