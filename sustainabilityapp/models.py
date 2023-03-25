from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('sustainabilityapp:profile', kwargs={})
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
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

