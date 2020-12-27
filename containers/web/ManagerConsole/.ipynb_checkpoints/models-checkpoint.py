from django.db import models


class Player(models.Model):
    def __str__(self):
        return self.name

    name = models.TextField(blank=True, null=True)
    id = models.TextField(unique=True, blank=True, primary_key=True)
    position = models.TextField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    shoots = models.TextField(blank=True, null=True)
    youth_team = models.TextField(db_column='youth team', blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    birth_country = models.TextField(blank=True, null=True)
    birth_city = models.TextField(blank=True, null=True)
    draft_entry = models.FloatField(blank=True, null=True)
    nhl_rights = models.TextField(blank=True, null=True)
    draft_team = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerSeasonStats(models.Model):
    def __str__(self):
        return f'{self.player} {self.season}'

    id = models.TextField(unique=True, blank=True, primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.TextField(blank=True, null=True)
    team = models.TextField(blank=True, null=True)
    league = models.TextField(blank=True, null=True)
    games = models.FloatField(blank=True, null=True)
    goals = models.FloatField(blank=True, null=True)
    assists = models.FloatField(blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    penalty = models.FloatField(blank=True, null=True)
    plus_minus = models.FloatField(blank=True, null=True)
    postseason_flag = models.BigIntegerField(blank=True, null=True)
    year = models.DateTimeField(blank=True, null=True)
    years_passed = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_season'
