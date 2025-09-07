from django import forms

from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields="__all__"


from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'review']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Review'}),
        }
