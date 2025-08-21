from django.shortcuts import render
from .forms import LaptopForm
from .models import Laptop

def add_view(request):
    form=LaptopForm()
    if request.method=="POST":
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
    template_name='laptop_app/add_laptop.html'
    context={"form":form}
    return render(request, template_name, context)

def show_view(request):
    laptop=Laptop.objects.all()
    template_name='laptop_app/show_laptop.html'
    context={"laptop":laptop}
    return render(request, template_name, context)
