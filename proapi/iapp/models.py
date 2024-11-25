from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField()