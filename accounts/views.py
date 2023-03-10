from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")            

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        phoneno=request.POST['phone no']
        password1=request.POST['password']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password1=password,password2=password,first_name=first_name,last_name=last_name,email=email)
        user.save();
        print("user created")
        return redirect('/')
    else:    
        
         return render(request,"registration.html")