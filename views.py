from django.shortcuts import render,redirect
from studentapp.models import Employee
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def empDetails(request):
    emp_data=Employee.objects.all()
    emp_dict={'emp_list':emp_data}
    return render(request,'register.html',context=emp_dict )



def Home(request):
    return render(request,'home.html')
#def Login(request):
    #return render(request,'login.html')

def Register(request):
    if request.method=='POST':
        name=request.POST["Username"]
        email=request.POST["email"]
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account created')
            return redirect('login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('register') 
        
       
    else:
        form=CreateUserForm()
        return render(request,'register.html',{'form':form})
@login_required      
def Profile(request):
    return render(request,'profile.html')
        
        

# Create your views here.
