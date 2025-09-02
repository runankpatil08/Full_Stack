from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def home_view(request):
    template_name='laptop_app/home.html'
    context={}
    return render(request, template_name, context)


def faq_view(request):
    template_name='laptop_app/faq.html'
    context={}
    return render(request, template_name, context)

def contact_view(request):
    template_name='laptop_app/contact.html'
    context={}
    return render(request, template_name, context)


@login_required
def add_view(request):
    form=LaptopForm()
    if request.method=="POST":
        form=LaptopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
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
            messages.warning(request, 'Update successful')
            return redirect('show')
    template_name='laptop_app/add_laptop.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required
def delete_view(request,id):
    laptop=Laptop.objects.get(id=id)
    laptop.delete()
    messages.error(request, 'Delete successful')
    return redirect('show')
