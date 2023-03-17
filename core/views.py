from django.shortcuts import render, redirect
from items.models import Item, Category
from .forms import UserRegisterForm
from django.contrib import messages
from django.db import models

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[0:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account "{username}" have been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'core/register.html', {'form': form})




