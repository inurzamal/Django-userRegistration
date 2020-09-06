from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from home.models import Registeration


def index(request):
    return render(request, 'index.html')

def loginuser(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'premium.html')

        else:
            return render(request, 'login.html', {'msg':'Inavlid username or password'})
    

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/')


def register(request):

    if request.method=="POST":
        name= request.POST['name']
        email= request.POST['email']
        username= request.POST['username']
        password= request.POST['password']
        phone= request.POST['phone']

        # Creating user using inbuilt model object from User, No need to create own models 
        user = User.objects.create_user(username=username, password=password)
        user.save()


        reg = Registeration(name= name,  email=email, username=username, password= password, phone=phone, date=datetime.today())
        reg.save()


        message = {'msg':'user created Succesfully !'}
        return render(request, 'register.html', message)



    return render(request, 'register.html')


