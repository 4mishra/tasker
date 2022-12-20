from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


def signup(request):
    # POST
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = request.POST.get("username")
            # password = request.POST.get("password1")
            # user = User.objects.create_user(
            #     username=username, password=password
            # )
            login(request, user)
            return redirect("home")
    # GET
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
