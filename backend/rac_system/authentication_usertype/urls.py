from django.urls import path, include
from . import views

"""urlpatterns = [
    path("login/",views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register')
]
"""

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('register/candidate/<int:user_id>/', views.candidate_register_extra, name='candidate_register_extra'),
    path('register/company/<int:user_id>/', views.company_register_extra, name='company_register_extra'),
    path('login/', views.login, name='login'),
]
