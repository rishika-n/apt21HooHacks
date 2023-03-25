from django.shortcuts import render
from .models import Profile
from django.views import generic

# Create your views here.

class ProfileView(generic.ListView):
    model = Profile
    template_name = 'sustainabilityapp/profile.html'
    context_object_name = 'my_profile'
    def get_queryset(self):
        """Return the last five published questions."""
        return Profile.objects.filter(user=self.request.user).last()
