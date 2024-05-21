from django.db import models
class Employee(models.Model):
    EmpNo=models.IntegerField()
    EmpName=models.CharField(max_length=20)
    EmpSal=models.IntegerField()
    empAddress=models.CharField(max_length=100)


# Create your models here.
