from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField( max_length=20)
    last_name = models.CharField( max_length=20)
    email = models.EmailField(max_length=100)
    message = models.TextField()
   

class StarOfWeek(models.Model):
    img = models.ImageField(null=True , blank=True)
    name = models.CharField( max_length=60)
    grade = models.IntegerField()