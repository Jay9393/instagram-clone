from django.urls import path, include

urlpatterns = [
    path("users", include("users.urls")),
    path("posts", include("posts.urls")),
    path("likes", include("likes.urls")),
    path("follows", include("follows.urls")),
]
