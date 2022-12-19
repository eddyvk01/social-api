from posts.models import Post
from likes.permissions import hasSelfVotedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Like
from . serializers import LikeSerializer


# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfVotedOrReadOnly]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post'])

        #if user likes the post
        if self.request.data['like']:
            already_liked=Like.objects.filter(post=post_instance,like=self.request.user).exists()
            if already_liked:
                raise serializers.ValidationError({"message":"You have already liked this post"})
            else:
                serializer.save(like=self.request.user,post=post_instance)
        #if dislikes
        else:
            already_disliked=Like.objects.filter(post=post_instance,unlike=self.request.user).exists()
            if already_disliked:
                raise serializers.ValidationError({"message":"You have already disliked this post"})
            else:
                serializer.save(unlike=self.request.user,post=post_instance)
        
