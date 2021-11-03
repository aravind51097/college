from django.db import models
from django.db.models import manager
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255)
    reg_num=models.BigIntegerField()
    dept=models.CharField(max_length=150)
    year_of_joining=models.DateField(auto_now_add=True)
    email=models.EmailField(default=False,null=True)
    ph_num=models.CharField(max_length=255,null=True)

class FirstSemSubjects(models.Model):
    english=models.IntegerField()
    maths=models.IntegerField()
    computer_science=models.IntegerField()
    electrical=models.IntegerField()
    student=models.OneToOneField(Student,primary_key=True,on_delete=CASCADE)

class SecondSemSubjects(models.Model):
    english=models.IntegerField()
    maths=models.IntegerField()
    environment_science=models.IntegerField()
    physics=models.IntegerField()
    student=models.OneToOneField(Student,primary_key=True,on_delete=CASCADE)



