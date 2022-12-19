from rest_framework.routers import DefaultRouter
from user_profile.views import ProfileViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet
from followers.views import followViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'profiles',ProfileViewSet)
router.register(r'followers',followViewSet)
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'likes',LikeViewSet)


urlpatterns = [
    path('user/', include('users.urls')),
]

urlpatterns += router.urls 
