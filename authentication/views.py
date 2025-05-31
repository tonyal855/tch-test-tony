from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Role, CustomAuth
from tech_test.decorator import role_required

# Create your views here.

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('module')  # Redirect to home page or dashboard
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "authentication/login.html")

def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required()
@role_required('manajer')
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role_id = request.POST.get('role')

        role = Role.objects.get(id=role_id)

        CustomAuth.objects.create_user(
            username=username,
            password=password,
            role_id=role,
            module_id=request.user.module_id
        )

        return redirect('module')

    role = Role.objects.all()
    return render(request, "authentication/create_user.html", {'roles': role})
