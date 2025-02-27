from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "auth_form.html", {"form_type": "login", "form": form})

def register_view(request):
    if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "auth_form.html", {"form_type": "register", "form": form})

def log_out(request):
    logout(request)
    return redirect("login")
