from django.shortcuts import render, redirect
from profiles.forms import RegisterForm
from django.contrib.auth.models import User
from profiles.models import Profile

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
            new_user = User.objects.create_user(username=form.cleaned_data["user_name"],
                                     email=form.cleaned_data["email"],
                                     password=form.cleaned_data["password"])
            new_profile = Profile.objects.create(user=new_user,
                                                 first_name=form.cleaned_data["first_name"],
                                                 last_name=form.cleaned_data["last_name"],
                                  )
            if form.cleaned_data["age"] is not None:
                new_profile.age = form.cleaned_data["age"]
                new_profile.save()

            logger.info(f'User email {form.cleaned_data["email"]}')
            logger.info(f'User password {form.cleaned_data["password"]}')
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})