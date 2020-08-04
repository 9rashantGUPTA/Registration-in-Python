from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm


def home(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account is done mr.{username}')
    else:
        form = UserRegisterForm()
    return render(request, 'user/home.html', {'form': form})
