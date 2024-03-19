from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,  auth
from django.contrib.auth import authenticate,login,logout
from myproject import settings
from .models import Lecturer
from .forms import LecturerForm,LecturerLogin
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def lecturer_home(request):
    lec_id = request.session.get('lec_id', None)
    lec = get_object_or_404(Lecturer, id=lec_id)
    context ={
        'lec_id': lec_id,
        'lec':lec,
    }
    
    return render(request, 'lec_index.html', context)

def landing(request):
    return render(request, 'landing.html')

def lecturer_signup(request):
    if request.method == 'POST':       
        form = LecturerForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            regno = form.cleaned_data['regno']
            img = form.cleaned_data['img']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if Lecturer.objects.filter(email=email).exists():
                messages.error(request, 'Email account already exists!')
                return redirect('lsignup')


            if password == confirm_password:
                hashed_password = make_password(password)
                user = Lecturer(fullname=fullname,email=email,regno=regno,img=img, password=hashed_password)
                
                user.save()  
                messages.success(request, 'Account Created Successfull!')              
                return redirect('lsignin')
            else:
                messages.error(request, 'passwords do not match.')
    else:
        form = LecturerForm()

    return render(request, 'l_signup.html', {'form': form})


def lecturer_signin(request):
    if request.method == 'POST':
        form = LecturerLogin(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                lec = Lecturer.objects.get(email=email)
                # user_id = request.session.get('user_id', None)

                if check_password(password, lec.password):                   
                    request.session['lec_id'] = lec.id
                    request.session['fullname'] = lec.fullname
                    return redirect('lhome')                    
                    
                else:
                    messages.error(request, 'Incorrect password.')

            except Lecturer.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')

    else:
        form = LecturerLogin()

    return render(request, 'l_signin.html', {'form': form})


def lecturer_logout(request):
    # Use Django's logout function to log the user out
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('lsignin')
