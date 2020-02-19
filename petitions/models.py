from django.db import models
from django.contrib.auth import get_user_model

STATUS_CHOICES = [
    ('a', 'Approved'),
    ('w', 'Waiting'),
    ('d', 'Denied'),
]


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=10000)
    author = models.CharField(max_length=300, default="Anonymous")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='w')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def votes_count(self):
        return self.votes.all().count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='w')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.body


class Vote(models.Model):
    class Meta:
        unique_together = [('post', 'user')]

    post = models.ForeignKey(Post, related_name='votes',
                             on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.__str__() + ": " + self.user.__str__();
