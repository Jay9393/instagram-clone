from django.urls import path
from follows.views import FollowView, GetFollowingView, UnFollowView, GetFollowerView

urlpatterns = [
    path("/following", FollowView.as_view()),
    path("/unfollowing", UnFollowView.as_view()),
    path("/getfollowing", GetFollowingView.as_view()),
    path("/getfollower", GetFollowerView.as_view()),
]
