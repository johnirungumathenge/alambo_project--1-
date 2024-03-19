from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,  auth
from django.contrib.auth import authenticate,login,logout
from myproject import settings
from .models import Supervisor, Approved_records
from .forms import SupervisorForm,SupervisorLogin,ApprovedRecordsForm
from django.contrib.auth.hashers import make_password, check_password
from student.models import UpdateDetails

# Create your views here.


def supervisor_home(request):
    sup_id = request.session.get('sup_id', None)
    supervisor = get_object_or_404(Supervisor, id=sup_id)
    context ={
        'sup_id': sup_id,
        'supervisor':supervisor,
    }
    
    return render(request, 's_home.html', context)

def landing(request):
    return render(request, 'landing.html')
    
def s_signup(request):
    if request.method == 'POST':       
        form = SupervisorForm(request.POST, request.FILES)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            regno = form.cleaned_data['regno']
            s_img = form.cleaned_data['img']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if Supervisor.objects.filter(email=email).exists():
                messages.error(request, 'Email account already exists!')
                return redirect('s_signup')


            if password == confirm_password:
                hashed_password = make_password(password)
                user = Supervisor(fullname=fullname,email=email,regno=regno,img=s_img, password=hashed_password)
                messages.success(request, 'Account Created Successfull!')
                user.save()                
                return redirect('s_signin')
            else:
                messages.error(request, 'passwords do not match.')
    else:
        form = SupervisorForm()

    return render(request, 's_signup.html', {'form': form})


def sup_signin(request):
    if request.method == 'POST':
        form = SupervisorLogin(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                sup = Supervisor.objects.get(email=email)
                # user_id = request.session.get('user_id', None)

                if check_password(password, sup.password):                   
                    request.session['sup_id'] = sup.id
                    request.session['fullname'] = sup.fullname
                    return redirect('sup_home')                    
                    
                else:
                    messages.error(request, 'Incorrect password.')

            except Supervisor.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')

    else:
        form = SupervisorLogin()

    return render(request, 's_signin.html', {'form': form})


def s_signout(request):
    # Use Django's logout function to log the user out
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('s_signin')

# requests made by students
def view_records(request):
    record = UpdateDetails.objects.all()
    context ={
        'record': record,
    }
    return render(request, 'records.html', context)
# approve users records
def approve_record(request, record_id):
    record = get_object_or_404(UpdateDetails, pk=record_id)
    if request.method == 'POST':
        
        form = ApprovedRecordsForm(request.POST)
        if form.is_valid():
            approved =form.cleaned_data['approved']
            form.save()
            # return redirect('view_records')
            
            if approved:  # Check if the record is approved
                record.delete()  # Delete the record
                return redirect('view_records')  # Redirect to a view after deleting the record
            else:
                return redirect('sup_home')  
            # record.delete()

        else:
            messages.error(request, 'failed to insert')
            return redirect('sup_home')  # Redirect to a view after saving the form
    else:
        form = ApprovedRecordsForm(instance=record)
    
    return render(request, 'approve_record.html', {'form': form})

# show reviewed
def reviewed_records(request):
    approved = Approved_records.objects.all()
    context ={
        'records': approved,
    }
    return render(request, 's_approved.html', context)