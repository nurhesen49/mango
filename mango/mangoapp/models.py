from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    potfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
