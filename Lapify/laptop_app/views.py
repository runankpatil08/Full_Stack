from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop

def add_view(request):
    form=LaptopForm()
    if request.method=="POST":
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='laptop_app/add_laptop.html'
    context={"form":form}
    return render(request, template_name, context)

def show_view(request):
    laptop=Laptop.objects.all()
    template_name='laptop_app/show_laptop.html'
    context={"laptop":laptop}
    return render(request, template_name, context)

def update_view(request,id):
    laptop=Laptop.objects.get(id=id)
    form=LaptopForm(instance=laptop)
    if request.method=="POST":
        form=LaptopForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='laptop_app/add_laptop.html'
    context={'form':form}
    return render(request, template_name, context)


def delete_view(request,id):
    laptop=Laptop.objects.get(id=id)
    laptop.delete()
    return redirect('show')
