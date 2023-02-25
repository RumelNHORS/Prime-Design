from django.shortcuts import render, redirect
from . models import ContactModel
from . forms import ContactForms


# Create your views here.

def indexView(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        sv = ContactModel(first_name=first_name, last_name=last_name, email=email, message=message)
        sv.save()
    return render(request, 'myapp/index.html')

"""
def contactView(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        sv = ContactModel(first_name=first_name, last_name=last_name, email=email, message=message)
        sv.save()
        return render(request, 'myapp/index.html')
    else:
          
        return render(request, 'myapp/contact.html')"""
        
def productView(request):
    return render(request, 'myapp/product.html')       
