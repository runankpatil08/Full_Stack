from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Testimonial
from .forms import TestimonialForm


def home_view(request):
    template_name = 'laptop_app/home.html'

    # Get top 3 latest laptops in stock (sorted by id descending)
    top_laptops = Laptop.objects.filter(stock__gt=0).order_by('-id')[:3]

    context = {
        'top_laptops': top_laptops
    }
    return render(request, template_name, context)


# ✅ New Static Pages
def faq_view(request):
    template_name='laptop_app/faq.html'
    context={}
    return render(request, template_name, context)

def contact_view(request):
    template_name='laptop_app/contact.html'
    context={}
    return render(request, template_name, context)

def career_view(request):
    template_name = 'laptop_app/career.html'
    return render(request, template_name)

def privacy_view(request):
    template_name = 'laptop_app/privacy.html'
    return render(request, template_name)


def terms_view(request):
    template_name = 'laptop_app/terms.html'
    return render(request, template_name)



def testimonials_view(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()

    context = {
        "testimonials": testimonials,
        "form": form,
    }
    return render(request, 'laptop_app/testimonials.html', context)


def shop_stock_user_see_view(request):
    query = request.GET.get("q")  # get search query from request
    if query:
        laptop = Laptop.objects.filter(company__icontains=query)  # search by brand/company name
    else:
        laptop = Laptop.objects.all()

    template_name = "laptop_app/showStockUser.html"
    context = {"laptop": laptop}
    return render(request, template_name, context)




@login_required
def add_view(request):
    form=LaptopForm()
    if request.method=="POST":
        form=LaptopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # ✅ Send email alert
            send_mail(
                'Test Email',
                'Hello! Your Product has been added.',
                'runankpatil08@gmail.com',  # From
                ['runankpatil2001@gmail.com'],  # To
                fail_silently=False,
            )
            messages.success(request, 'add successful')
            return redirect('show')
    template_name='laptop_app/add_laptop.html'
    context={"form":form}
    return render(request, template_name, context)

@login_required
def show_view(request):
    laptop=Laptop.objects.all()
    template_name='laptop_app/show_laptop.html'
    context={"laptop":laptop}
    return render(request, template_name, context)


@login_required
def update_view(request,id):
    laptop=Laptop.objects.get(id=id)
    form=LaptopForm(instance=laptop)
    if request.method=="POST":
        form=LaptopForm(request.POST,request.FILES,instance=laptop)
        if form.is_valid():
            form.save()

            # ✅ Send email alert
            send_mail(
                'Test Email',
                'Hello! Your Product has been updated.',
                'runankpatil08@gmail.com',  # From
                ['runankpatil2001@gmail.com'],  # To
                fail_silently=False,
            )
            messages.warning(request, 'Update successful')
            return redirect('show')
    template_name='laptop_app/add_laptop.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required
def delete_view(request,id):
    laptop=Laptop.objects.get(id=id)
    laptop.delete()

    # ✅ Send email alert
    send_mail(
        'Test Email',
        'Hello! Your Product has been delete.',
        'runankpatil08@gmail.com',  # From
        ['runankpatil2001@gmail.com'],  # To
        fail_silently=False,
    )
    messages.error(request, 'Delete successful')
    return redirect('show')
