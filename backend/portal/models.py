from django.db import models

# Create your models here.


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=120)


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    releaseYear = models.IntegerField()
    publisher = models.CharField(max_length=120)
    logoUrl = models.CharField(max_length=480)


class GameTag(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
