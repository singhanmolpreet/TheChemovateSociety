from django.shortcuts import render
from .models import Event
from datetime import date


def homepage(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


def events(request):
    pass

def upcoming_events(request):
    events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'core/upcoming_events.html', {'events': events})


def previous_events(request):
    pass


def login(request):
    pass