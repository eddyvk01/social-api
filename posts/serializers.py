from . models import Post
from rest_framework import serializers
from  comments.serializers import CommentSerializer
from likes.serializers import LikeSerializer
class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    likes =LikeSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'content','post_image','category','post_date','likes','comments']

        