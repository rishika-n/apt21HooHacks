from django.urls import path, include
from . import views
# from django_crontab import urls



app_name = 'sustainabilityapp'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    #path('')
]

