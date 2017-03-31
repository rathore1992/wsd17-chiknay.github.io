from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    activationToken = models.CharField(max_length=36)

    @property
    def is_player(self):
        return self.user.groups.filter(name='players').exists()

    @property
    def is_developer(self):
        return self.user.groups.filter(name='developers').exists()

    def __str__(self):
        return str(self.user.username)