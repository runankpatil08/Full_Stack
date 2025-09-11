from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect

from django.contrib import messages
from django.core.mail import send_mail
from .forms import CustomUserCreationForm



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ✅ Send email alert
            send_mail(
                'Test Email',
                f'Hello {user.username},\n\n you have Successfully Registered on LapiFy ',
                'runankpatil08@gmail.com',  # From
                [user.email],  # To
                fail_silently=False,
            )

            login(request, user)  # optional: auto-login after registration
            messages.success(request, "Account created successfully!")
            return redirect("home")  # change to your homepage
    else:
        form = CustomUserCreationForm()
    return render(request, "auth_app/register.html", {"form": form})




def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Login Successful')

            # ✅ Send email alert
            send_mail(
                subject='Login Alert - LapiFy',
                message=f'Hello {user.username},\n\n you have Successfully Log In if this is not you secure your account ',
                from_email='runankpatil08@gmail.com',   # Replace with your EMAIL_HOST_USER
                recipient_list=[user.email],  # Can also be [user.email]
                fail_silently=False,
            )

            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    template_name = 'auth_app/login.html'
    context = {}
    return render(request, template_name, context)



def logout_view(request):
    logout(request)
    messages.error(request,'Logout successful',extra_tags='error')
    return redirect('home')


