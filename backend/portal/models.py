from django.db import models

# Create your models here.

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=120)