from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class GamesModel(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    url = models.URLField(unique=True)
    price = models.FloatField(default=0)
    publicationDate = models.DateTimeField(default=timezone.now)
    logo = models.URLField(default="http://give path of imge")
    popularity = models.IntegerField(default=0)
    _developer = models.ForeignKey('Users.Profile', null=False)

    def __str__(self):
        return str(self.name)

    def to_json_dict(self, user=None):
        res = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'publicationDate': str(self.publicationDate),
            'popularity': self.popularity,
            'logo': self.logo,
            'developer': self._developer.user.username,
        }

        if user is not None and isinstance(user, User):
            owned = False
            o = user.profile._ownedGames.filter(id=self.id)
            if o.count()>0:
                res['owned'] = True
            else:
                res['owned'] = False

        return res
