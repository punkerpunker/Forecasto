from django.db import models


class Player(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    age = models.IntegerField()
    nationality = models.CharField(max_length=150)
    position = models.CharField(max_length=8)


class PlayerSeasonStats(models.Model):
    def __str__(self):
        return f'{self.player} {self.season_year}'

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    games = models.IntegerField()
    points = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    season_year = models.IntegerField()
    team_name = models.CharField(max_length=30)
