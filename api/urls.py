from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.StudentListCreateView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),
    path('courses/', views.CourseListCreateView.as_view()),
    path('course/<int:pk>/', views.CourseDetailView.as_view()),
]
