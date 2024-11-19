from django.db import models
from posts.models import Post, get_default_owner
from django.contrib.auth.models import User

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE, default=get_default_owner)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} likes {self.post}'