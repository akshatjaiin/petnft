from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, PetForm, PetImageForm
from .models import User, Pet, PetPost

# Home View
def index(request):
    if request.user.is_authenticated:
        return render(request, "petapp/index.html")
    else:
        return HttpResponseRedirect(reverse("petapp:register"))

# Login View
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "petapp/login.html", {
                "message": "Invalid username and/or password."
            })
    
    return render(request, "petapp/login.html")


# Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# User Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('index')
            except IntegrityError:
                messages.error(request, 'A user with this username already exists. try to login')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form for errors.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'petapp/register.html', {'form': form})




# User Profile Edit View
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'petapp/edit_profile.html', {'form': form})


# User Profile View
@login_required
def profile(request):
    return render(request, 'petapp/profile.html', {'user': request.user})


# Pet Creation View
@login_required
def create_pet(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.owner = request.user
            pet.save()
            messages.success(request, 'Pet added successfully.')
            return redirect('petapp:pet_detail', pet_id=pet.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        pet_form = PetForm()

    return render(request, 'petapp/create_pet.html', {'pet_form': pet_form})


@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'petapp/pet_detail.html', {'pet': pet})


@login_required
def adopt(request):
    return render(request, 'petapp/adopt.html')

@login_required
def swipe(request):
    return render(request, 'petapp/swipe.html', {
        'pet': pet,
        })