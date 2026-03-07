from django.db import models
from django.forms import IntegerField



class Course(models.Model):
    name = models.CharField(max_length=500)
    duration = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Students(models.Model):
    name = models.CharField(max_length=500)
    email=models.EmailField(unique=True,null=False,blank=False)
    age=models.IntegerField()
    course = models.ManyToManyField(Course,null=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    