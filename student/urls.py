from django.urls import path
from . import views

urlpatterns =[
    path('',views.landing, name='landing'),
    path('home', views.home, name="home"),
    path('signup', views.Signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('update_record', views.add_details, name='add_record'),
    path('view_record', views.view_data, name='view_data'),
    path('update_record/<int:record_id>/', views.update_details, name='update_record'),
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),
    path('approved', views.approved, name='approved'),
]