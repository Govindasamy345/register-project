
from django.contrib import admin
from studentapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    emp_list=['EmpNo','EmpName','EmpSal','empAddress']
    
admin.site.register(Employee,EmployeeAdmin)

# Register your models here.