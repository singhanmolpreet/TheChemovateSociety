from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from rac_system import settings
from django.contrib import messages


def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        '''if User.objects.filter(email=email):
            messages.error(request, "Email already registered!!")
            return redirect('signup')
        '''
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('signup')
        
        if pass1!=pass2:
            messages.error(request,"Your password and confirm password are not Same!!")
        

        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            #messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email, please confirm to complete registration.")

            # Welcome Email
        
            subject = "Welcome to Match Maestro"
            message = "Welcome to Match Maestro \n" + "Please confirm your email in order to authenticate your account \n" + "Thanking you \n" + "Team Match Maestro \n"
            from_email = settings.EMAIL_HOST_USER
            to_list = [my_user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
        
            #return HttpResponse('Please confirm your email address to complete the registration')

        #return redirect('login')

    return render (request,'authentication/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user) 
            return redirect('upload_and_match')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'authentication/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

