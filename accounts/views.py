from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect


def login_user(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=email, 
            password=password
        )

        if user is not None:

            auth_login(request, user)

            return redirect("home")

    return render(request, "accounts/login.html")


def register(request):

    if request.method == "POST":

        full_name = request.POST["full_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:

            User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name
            )

            return redirect("login")

    return render(request, "accounts/register.html")

def logout_user(request):
    logout(request)
    return redirect("home")