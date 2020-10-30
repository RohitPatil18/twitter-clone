from django.db import models
from users.models import User


class Tweet(models.Model):
    """
    Primary table to store tweets
    """
    tweet_text = models.CharField(max_length=250)
    parent_tweet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)  
    likes = models.ManyToManyField(
        User,
        through='TweetLike',
        through_fields=('tweet', 'user')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweeted_by')

    def __str__(self):
        return self.tweet_text

    class Meta:
        db_table = 'tweet'


class TweetLike(models.Model):
    """
    Mapping table for tweets liked by users
    """
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tweet_likes'
        verbose_name_plural = 'Tweet Likes'
        unique_together = ('tweet', 'user')

    def __str__(self):
        return f'Tweet ID : {self.tweet_id} liked by {self.user.name}'