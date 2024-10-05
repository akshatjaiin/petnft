from django.urls import path
from . import views
app_name = 'petapp'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('addPet', views.create_pet, name='add_pet'),
    path('adopt', views.adopt, name='adopt'),
    path('swipe', views.swipe, name='swipe'),
    path('market', views.market, name='marketplace'),
    path('chat', views.chat, name='chat'),
    path('daycare', views.daycare, name='daycare'),
    path('customize', views.customize, name='customize'),
    path('settings', views.settings, name='settings'),
    path('petstore', views.petstore, name='petstore'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),

]
