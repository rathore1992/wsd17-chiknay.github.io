from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    registration_date = models.DateTimeField(auto_now_add=True)


class Game(models.Model):
    name = models.CharField(max_length=256)


class Score(models.Model):
    game = models.ForeignKey(Game)


class Sale(models.Model):
    game = models.ForeignKey(Game)