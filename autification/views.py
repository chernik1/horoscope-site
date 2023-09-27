from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from autification.forms import LoginForm

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/table/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    return render(request, 'autification/logout.html')

def register(request):
    return render(request, 'autification/register.html')