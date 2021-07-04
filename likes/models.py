from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE

from users.models              import User
from posts.models              import Comment,Post

class Like(models.Model):
    post       = models.ForeignKey('posts.Post', related_name='posts_like', on_delete=CASCADE, null=True)
    comment    = models.ForeignKey('posts.Comment', related_name='comments_like', on_delete=CASCADE, null=True)
    user       = models.ForeignKey('users.User', related_name='like_user', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'