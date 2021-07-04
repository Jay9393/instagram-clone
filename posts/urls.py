from django.urls import path
from posts.views import PostView, CommentPost, CommentView, NestedPost, NestedView

urlpatterns = [
    path("/posting", PostView.as_view()),
    path("/comment/post", CommentPost.as_view()),
    path("/comment/view", CommentView.as_view()),
    path("/nested/post", NestedPost.as_view()),
    path("/nested/view", NestedView.as_view()),
]
