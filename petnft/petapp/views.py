from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import  CustomUserChangeForm, PetForm, PetImageForm
from .models import User, Pet, PetPost

# Home View
def index(request):
    print(f"trying to print username {request.user.username}")
    if request.user.is_authenticated:
        return render(request, "petapp/index.html")
    else:
        return HttpResponseRedirect(reverse("petapp:register"))
def login_view(request):
    if request.method == "POST":
        # Get username and password from the form
        username = request.POST["username"]
        password = request.POST["password"]
        # Attempt to authenticate the user
        user = authenticate(request, username=username, password=password)
        print(f"{username} and {password}")
        print(f'user {user}')

        # Check if authentication was successful
        if user is not None:
            login(request, user)  # login() requires both request and user objects
            return HttpResponseRedirect(reverse("petapp:index"))
        else:
            # If authentication fails, return the form with an error message
            return render(request, "petapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "petapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("petapp:index"))

def register(request):
    if request.method == "POST":
        # Extract form data
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "petapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            print(f"user saved .. {username} {email} {password}")
            user.save()  # Save user to the database
            print('saved user...')

            # Log the user in after successful registration
            login(request, user)  # login() requires the request and user object
            print("user login success ... ")

            # Redirect to the index page
            return HttpResponseRedirect(reverse("petapp:index"))

        except IntegrityError:
            # Handle the case when the username is already taken
            return render(request, "petapp/register.html", {
                "message": "Username already taken."
            })

    else:
        # Render the registration form
        return render(request, "petapp/register.html")

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

@login_required
def edit_profile(request):
    return render(request, 'petapp/swipe.html', {
        'pet': pet,
        })

@login_required
def market(request):
    return render(request, 'petapp/market.html', {
        'pet': 'petsnft',
        })

@login_required
def chat(request):
    return render(request, 'petapp/chat.html', {
        'pet': 'petsnft',
        })
@login_required
def customize(request):
    return render(request, 'petapp/chat.html', {
        'pet': 'petsnft',
        })

@login_required
def daycare(request):
    return render(request, 'petapp/chat.html', {
        'pet': 'petsnft',
        })

@login_required
def petstore(request):
    return render(request, 'petapp/chat.html', {
        'pet': 'petsnft',
        })

@login_required
def settings(request):
    return render(request, 'petapp/settings.html', {
        'settings': 'settings',
        })