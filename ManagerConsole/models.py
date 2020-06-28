from django.db import models


class Player(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    position = models.CharField(max_length=2)

