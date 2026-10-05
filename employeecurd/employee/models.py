from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    gender_q=[
        ('male','Male'),('female','Female')
    ]
    gender= models.CharField(max_length=30,choices=gender_q)
    joindate=models.DateField(auto_now=True)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)