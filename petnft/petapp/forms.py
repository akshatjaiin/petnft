from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Pet, PetPost

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'profile_image')

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'description', 'breed', 'public', 'adopt', 'petpfp', 'category', 'age']

class PetImageForm(forms.ModelForm):
    class Meta:
        model = PetPost
        fields = ['image', 'title', 'description']