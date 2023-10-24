from django.shortcuts import render, redirect
from .models import Contact, Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        description = request.POST.get('description')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.description = description
        contact.save()
        return redirect('home')
    context = {
        'project': projects
    }
    return render(request, 'index.html', context)
