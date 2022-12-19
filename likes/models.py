from django.db import models
from posts.models import Post
# Create your models here.
class Like(models.Model):
    post=models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    like = models.ForeignKey('users.User',related_name='like',on_delete=models.CASCADE,default=None,blank=True,null=True)
    unlike=models.ForeignKey('users.User',related_name='unlike',on_delete=models.CASCADE,default=None,blank=True,null=True)
    def __str__(self):
        return self.post.content