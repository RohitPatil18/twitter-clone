from django.db import models
from users.models import User


class UserFollower(models.Model):
    """
    Mapping table for user and his/her follower
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follower')

    class Meta:
        db_table = 'user_followers'
        verbose_name = 'User Follower'
        verbose_name_plural = 'User Followers'
        unique_together = ('user', 'follower')

    def __str__(self):
        return f'{self.follower.name} follows {self.user.name}.'