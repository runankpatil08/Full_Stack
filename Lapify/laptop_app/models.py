from django.db import models

class Laptop(models.Model):
    company = models.CharField(max_length=50)
    ram = models.PositiveIntegerField(help_text="RAM size in GB")
    storage = models.PositiveIntegerField(help_text="Storage in GB")
    color=models.CharField(max_length=20)
    stock=models.IntegerField()
    price=models.IntegerField()
    image = models.ImageField(upload_to='image', null=True, blank=True)

