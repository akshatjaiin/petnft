from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# User model
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='petapp_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='petapp_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    zodiac_sign = models.CharField(max_length=20, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


# Category
class Animal(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


# Likes
class Like(models.Model):
    like_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", db_constraint=False)

# db_constraint=False

# Pets
class Pet(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    breed = models.CharField(max_length=40, null=True)  # Make sure it's required
    public = models.BooleanField(default=True)
    adopt = models.BooleanField(default=True)
    petpfp = models.ImageField(upload_to='pet_pfp/', null=True)  # Required image field
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets", db_constraint=False)
    category = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="pets", db_constraint=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True) 
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)], null=True)
    
    def __str__(self):
        return self.name


# Pet Images
class PetPost(models.Model):
    pet_details = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="images", db_constraint=False)
    image = models.ImageField(upload_to='pet_images/', null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.title} "


# Messages
class Message(models.Model):
    text = models.CharField(max_length=1300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False, related_name="messages")
    message_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.author.username}"



# Matches
class Match(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_initiated",  db_constraint=False)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_received", db_constraint=False)
    pet1 = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="matches_as_pet1", db_constraint=False)
    pet2 = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="matches_as_pet2", db_constraint=False)
    matched_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match between {self.pet1.name} and {self.pet2.name}"