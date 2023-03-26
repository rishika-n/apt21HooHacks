from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField
import datetime
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    def __str__(self):
        return self.first_name + self.last_name
    
    def get_absolute_url(self):
        return reverse('sustainabilityapp:profile', kwargs={})
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)
    first_name = models.CharField(max_length=200, default='Alex')
    last_name = models.CharField(max_length=200, default='Smith')
    daily_progress = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    ch1Complete = models.BooleanField(default=False)
    ch2Complete = models.BooleanField(default=False)
    ch3Complete = models.BooleanField(default=False)
    ch4Complete = models.BooleanField(default=False)
    ch5Complete = models.BooleanField(default=False)
    ch6Complete = models.BooleanField(default=False)

    # """ INTEREST_CHOICES = (
    #     ('0', 'Climate Change'),
    #     ('1', 'Renewable Energy'),
    #     ('2', 'Gardening'),
    #     ('3','Water Conservation'),
    #     ('4', 'Secondhand Apparel'),
    #     ('5', 'Recycling'),
    #     ('6', 'Local Produce'),
    #     ('7', 'Supporting Sustainable Businesses'),
    #     ('8', 'Composting'),
    #     ('9', 'Plastic-Free'),
    #     ('10', 'Carpooling'),
    #     ('11', 'Public Transportation'),
    #     ('12', 'Awareness'),
    #     ('13', 'Veganism'),
    #     ('14', 'Biodegradable Products'),
    #     ('15', 'Animal Lover'),
    #     ('16', 'Tree Hugger'),
    #     ('17', 'Farmers Markets'),
    #     ('18', 'Ocean Conservation'),
    #     ('19', 'Reducing Carbon Footprint'),
    #     ('20', 'Anti-Littering'),
    #     ('21', 'Food Waste'),
    # ) """
    


    
        
class Friends(models.Model):
    users1=models.ManyToManyField(User,null=True)
    current_user=models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE,null=True)



    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend,create=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users1.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users1.remove(new_friend)
 
    



    
class FriendRequest(models.Model):
    sender=models.ForeignKey(User,null=True,related_name='sender1',on_delete=models.CASCADE)
    receiver=models.ForeignKey(User,null=True,on_delete=models.CASCADE)


class Challenges(models.Model):
    day = models.DateField(max_length=1000)
    ch1 = models.CharField(max_length=1000)
    ch2 = models.CharField(max_length=1000)
    ch3 = models.CharField(max_length=1000)
    ch4 = models.CharField(max_length=1000)
    ch5 = models.CharField(max_length=1000)
    ch6 = models.CharField(max_length=1000)