from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/', views.LogoutPage,name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login1/', views.LoginPage1,name='login1'),   
]
   