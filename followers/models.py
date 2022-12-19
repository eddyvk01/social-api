from django.db import models
from user_profile.models import UserProfile
# Create your models here.
class follow(models.Model):
    profile=models.ForeignKey(UserProfile,related_name='follow',on_delete=models.CASCADE)
    follow = models.ForeignKey('users.User',related_name='follow',on_delete=models.CASCADE,default=None,blank=True,null=True)
    unfollow=models.ForeignKey('users.User',related_name='unfollow',on_delete=models.CASCADE,default=None,blank=True,null=True)
    