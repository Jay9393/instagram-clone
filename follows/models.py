from django.db import models
from django.db.models.deletion import CASCADE

class Follow(models.Model):
    user = models.ForeignKey('users.User', related_name='follwer',on_delete=CASCADE)
    following = models.ForeignKey('users.User', related_name='following',on_delete=CASCADE)

    class Meta:
        db_table = 'follows'
