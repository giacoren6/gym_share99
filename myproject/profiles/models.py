from django.db import models
from django.contrib.auth.models import User

def get_default_owner():
    return User.objects.first() or User.objects.create(username='default_user', password='default_password')

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=get_default_owner)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="profile_images", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.owner.username