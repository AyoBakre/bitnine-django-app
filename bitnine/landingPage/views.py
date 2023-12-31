from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'landingPage/home.html', {'user': request.user})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'landingPage/register.html', context)