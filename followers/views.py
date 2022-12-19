from user_profile.models import UserProfile
from likes.permissions import hasSelfVotedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,permissions
from . models import follow
from . serializers import followSerializer


# Create your views here.
class followViewSet(viewsets.ModelViewSet):
    queryset=follow.objects.all()
    serializer_class=followSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfVotedOrReadOnly]
    def perform_create(self, serializer):
        profile_instance=get_object_or_404(UserProfile,pk=self.request.data['profile'])

        #if user follow the user
        if self.request.data['follow']:
            already_follow=follow.objects.filter(profile=profile_instance,follow=self.request.user).exists()
            if already_follow:
                raise serializers.ValidationError({"message":"You have already followed this user"})
            else:
                serializer.save(follow=self.request.user,profile=profile_instance)
        #if unfollow
        else:
            already_unfollow=follow.objects.filter(profile=profile_instance,unfollow=self.request.user).exists()
            if already_unfollow:
                raise serializers.ValidationError({"message":"You have already unfollow this user"})
            else:
                serializer.save(unfollow=self.request.user,profile=profile_instance)
        
