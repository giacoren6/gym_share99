from django.db import models
from django.contrib.auth.models import User

def get_default_owner():
    return User.objects.first() or User.objects.create(username='default_user', password='default_password')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, default=get_default_owner)

    def __str__(self):
        return self.title