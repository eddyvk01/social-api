from .models import UserProfile
from rest_framework import serializers
from followers.serializers import followSerializer

class ProfileSerializer(serializers.ModelSerializer):
    follower = followSerializer(many= True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model=UserProfile
        fields=['id', 'owner','follower','gender','dob','phone','works_at','lives_in','studies_at','profile_image']