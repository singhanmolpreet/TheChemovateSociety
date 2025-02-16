from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name="login"),
    path("events/", views.events, name="events"),
    path("events/upcoming/)", views.upcoming_events, name="upcoming_events"),
    path("events/previous/)", views.previous_events, name="previous_events"),
]

