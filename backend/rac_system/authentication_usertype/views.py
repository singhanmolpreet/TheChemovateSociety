from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, CandidateExtraForm, CompanyExtraForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            if user.role == 'CANDIDATE':
                return redirect('candidate_register_extra', user_id=user.id)
            else:
                return redirect('company_register_extra', user_id=user.id)
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def candidate_register_extra(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = CandidateExtraForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')  # Redirect to login after registration
        else:
            return render(request, 'candidate_extra.html', {'form': form, 'error': 'Invalid input. Please correct the errors below.'})
    else:
        form = CandidateExtraForm()
    return render(request, 'candidate_extra.html', {'form': form})


def company_register_extra(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CompanyExtraForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = CompanyExtraForm()
    return render(request, 'company_extra.html', {'form': form})

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home/dashboard page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
