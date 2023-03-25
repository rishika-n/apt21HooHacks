from django.urls import path, include
from . import views

app_name = 'sustainabilityapp'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]