from django.shortcuts import render
from .models import Profile, Challenges
from django.views import generic
# from django.utils import timezone
from pytz import timezone
import random
import schedule 
import time
from datetime import datetime

# Create your views here.

class ProfileView(generic.ListView):
    model = Profile
    template_name = 'sustainabilityapp/profile.html'
    context_object_name = 'my_profile'
    def get_queryset(self):
        """Return the last five published questions."""
        return Profile.objects.filter(user=self.request.user).last()

def homePage(request):
    todayest = timezone('EST')
    today = datetime.now(todayest).date()
    if Challenges.objects.count() == 0:
        set = Challenges(day=datetime.now(todayest).date())
        arrChallenges = updateChallenges()
        set.ch1 = arrChallenges[0]
        set.ch2 = arrChallenges[1]
        set.ch3 = arrChallenges[2]
        set.ch4 = arrChallenges[3]
        set.ch5 = arrChallenges[4]
        set.ch6 = arrChallenges[5]
        set.save()
    else:
        thisCH = Challenges.objects.get(pk=1)
        arrChallenges = [thisCH.ch1, thisCH.ch2, thisCH.ch3, thisCH.ch4, thisCH.ch5, thisCH.ch6]
    # today = datetime.strptime('03-28-2023', '%m-%d-%Y').date()
    # print("Today: ", today)
    # print("Latest Challenge Day:", Challenges.objects.get(pk=1).day)
    if today > Challenges.objects.get(pk=1).day:
        set = Challenges.objects.get(pk=1)
        arrChallenges = updateChallenges()
        set.ch1 = arrChallenges[0]
        set.ch2 = arrChallenges[1]
        set.ch3 = arrChallenges[2]
        set.ch4 = arrChallenges[3]
        set.ch5 = arrChallenges[4]
        set.ch6 = arrChallenges[5]
        set.day = datetime.now(todayest).date()
        set.save()
    return render(request, 'sustainabilityapp/home.html', {'challenges':arrChallenges})

def updateChallenges():
    with open("sustainabilityapp/challenges.txt", "r") as f:
        challenges = {}
        i = 0
        for challenge in f:
            i += 1
            challenges[i] = challenge.strip('\n').strip()
    random_numbers = random.sample(range(1, i), 6)
    ind = 0
    todaysChallenges = [0]*6
    for r in random_numbers:
        todaysChallenges[ind] = challenges[r]
        ind +=1
    return todaysChallenges
