from .models import follow
from rest_framework import serializers

class followSerializer(serializers.ModelSerializer):
    follow = serializers.ReadOnlyField(source='follow.username')
    unfollow=serializers.ReadOnlyField(source='unfollow.username')
    class Meta:
        model = follow
        fields = ['id','profile','follow','unfollow']

