from django.urls import path
from .import views

app_name = 'students'
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('courses/',views.courses,name='courses'),
    path('register-course/<int:pk>',views.register_course,name='register_course'),
    path('logout/',views.logout,name='logout'),
    
]
