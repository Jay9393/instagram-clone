from typing                     import Tuple
from django.db                  import models
from django.db.models.deletion  import CASCADE
from django.db.models.fields import related

from users.models               import User

class Post(models.Model):
    img             = models.URLField(max_length=1000)
    content         = models.TextField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user            = models.ForeignKey('users.User', related_name="posts", on_delete=CASCADE)
    like_count      = models.IntegerField(null=True)
    
    class Meta:
        db_table    = 'posts'

class Comment(models.Model):
    content         = models.TextField()
    post            = models.ForeignKey('posts.Post', related_name='main_comments', on_delete=CASCADE)
    users           = models.ForeignKey('users.User', related_name='user_comments', on_delete=CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    comment         = models.ForeignKey('posts.Comment', related_name="nested_comments", on_delete=CASCADE, null=True)
    like_count      = models.IntegerField(null=True)

    class Meta:
        db_table    = 'comments'