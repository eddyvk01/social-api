from .models import Like
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    like = serializers.ReadOnlyField(source='like.username')
    unlike=serializers.ReadOnlyField(source='unlike.username')
    class Meta:
        model = Like
        fields = ['id','post','like','unlike']

