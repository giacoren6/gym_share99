from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, get_default_owner

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, default=get_default_owner)

    def __str__(self):
        return f'{self.owner} comments {self.post}'