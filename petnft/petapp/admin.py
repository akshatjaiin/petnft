from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Animal, Like, Pet, PetPost, Message, Match


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('date_of_birth', 'bio', 'zodiac_sign', 'interests', 'profile_image',)
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'like_count')
    search_fields = ('user__username', 'user__email')

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'public', 'adopt', 'owner', 'category', 'created_at', 'age')
    search_fields = ('name', 'breed', 'owner__username', 'category__category_name')
    list_filter = ('public', 'adopt', 'category')
    autocomplete_fields = ('owner', 'category')

class PetPostAdmin(admin.ModelAdmin):
    list_display = ('pet_details', 'title', 'description')
    search_fields = ('pet__name', 'name')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'message_created_at')
    search_fields = ('author__username', 'pet__name', 'message')
    list_filter = ('message_created_at',)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'pet1', 'pet2', 'matched_on')
    search_fields = ('user1__username', 'user2__username', 'pet1__name', 'pet2__name')
    list_filter = ('matched_on',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(PetPost, PetPostAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Match, MatchAdmin)