from django.urls import path
from . import views

urlpatterns =[
    path('sup', views.supervisor_home, name='sup_home'),
    path('sup_signin', views.sup_signin, name='s_signin'),
    path('sup_signup', views.s_signup, name='s_signup'),
    path('sup-signout', views.s_signout, name='sup_signout'),
    path('approve_record/<int:record_id>/', views.approve_record, name='approve_record'),
    path('view_record', views.view_records, name="view_records"),
    path("reviewed_records", views.reviewed_records, name='reviewed_records' ),
]