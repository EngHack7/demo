from django.shortcuts import render
from .models import StarOfWeek

# Create your views here.
def Home(request):
    
    return render(request , 'main/home.html')

def Contact(request):
    return render(request , 'main/contact.html')


def About(request):
    return render(request , 'main/about.html')

def Stars(request):
    context ={}
    context['starsb'] = True 
    context["stars"] = StarOfWeek.objects.all()
    return render(request , 'main/starOfWeek.html' , context)
    