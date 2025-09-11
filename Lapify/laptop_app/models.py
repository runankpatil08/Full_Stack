from django.db import models
from django.conf import settings   # <-- to link with logged-in user

class Laptop(models.Model):
    company = models.CharField(max_length=50)
    ram = models.PositiveIntegerField(help_text="RAM size in GB")
    storage = models.PositiveIntegerField(help_text="Storage in GB")
    color = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.review[:30]}"
