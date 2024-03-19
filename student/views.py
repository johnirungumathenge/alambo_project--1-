from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,  auth
from django.contrib.auth import authenticate,login,logout
from myproject import settings
from .models import Student, UpdateDetails
from .forms import StudentForm,StudentLogin, UpdateDetailsForm
from django.contrib.auth.hashers import make_password, check_password
from supervisor.models import Approved_records
# Create your views here.


def home(request):
    user_id = request.session.get('user_id', None)
    student = get_object_or_404(Student, id=user_id)
    context ={
        'user_id': user_id,
        'student':student,
    }
    
    return render(request, 'index.html', context)

def landing(request):
    return render(request, 'landing.html')
    
def Signup(request):
    if request.method == 'POST':       
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['Fullname']
            email = form.cleaned_data['Email']
            regno = form.cleaned_data['Regno']
            profile = form.cleaned_data['Profile']
            password = form.cleaned_data['Password']
            confirm_password = form.cleaned_data['confirm_password']

            if Student.objects.filter(Email=email).exists():
                messages.error(request, 'Email account already exists!')
                return redirect('signup')


            if password == confirm_password:
                hashed_password = make_password(password)
                user = Student(Fullname=fullname,Email=email,Regno=regno,Profile=profile, Password=hashed_password)
                messages.success(request, 'Account Created Successfull!')
                user.save()                
                return redirect('signin')
            else:
                messages.error(request, 'passwords do not match.')
    else:
        form = StudentForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = Student.objects.get(Email=email)
                # user_id = request.session.get('user_id', None)

                if check_password(password, user.Password):                   
                    request.session['user_id'] = user.id
                    request.session['Fullname'] = user.Fullname
                    return redirect('home')                    
                    
                else:
                    messages.error(request, 'Incorrect password.')

            except Student.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')

    else:
        form = StudentLogin()

    return render(request, 'signin.html', {'form': form})


def signout(request):
    # Use Django's logout function to log the user out
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('signin')

# update details
def add_details(request):
    if request.method == 'POST':
        form = UpdateDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated record successful")
            return redirect('view_data')
    else:
        form = UpdateDetailsForm()
    return render(request, 'add_record.html', {'form':form})

# show updated data
# view updated data
def view_data(request):
    data = UpdateDetails.objects.all()
    context ={
        'data': data,
    }
    return render(request, 'view.html', context)

# update the records
def update_details(request, record_id):
    record = get_object_or_404(UpdateDetails, pk=record_id)
    if request.method == 'POST':
        form = UpdateDetailsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('view_data')
    else:
        form = UpdateDetailsForm(instance=record)
    return render(request, 'update_record.html', {'form': form})

# delete the updated record
def delete_record(request, record_id):
    record = get_object_or_404(UpdateDetails, pk=record_id)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('view_data')  # Redirect to the view_data page or any other URL after deletion
    return render(request, 'delete_record.html', {'record': record})

# approved records
def approved(request):
    approved = Approved_records.objects.all()
    context ={
        'records': approved,
    }
    return render(request, 'approved.html', context)