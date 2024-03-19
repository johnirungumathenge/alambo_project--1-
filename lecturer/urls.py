from django.urls import path
from . import views

urlpatterns =[
    path("lec", views.lecturer_home, name='lhome'),
    path("lecturer_signup", views.lecturer_signup, name='lsignup'),
    path("lecturer_signin", views.lecturer_signin, name='lsignin'),
    path("logout", views.lecturer_logout, name='logout'),
]