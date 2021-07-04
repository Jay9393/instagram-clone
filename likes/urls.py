from django.urls import path
from likes.views import CommentLikeView, PostLikeView, PostUnLikeView

urlpatterns = [
    path("/post", PostLikeView.as_view()),
    path("/post_un", PostUnLikeView.as_view()),
    path("/comment", CommentLikeView.as_view())
]
