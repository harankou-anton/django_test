from django.shortcuts import render, redirect
from profiles.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profile(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profile page")


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(email=form.cleaned_data["email"], username=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login_view")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
