from django.db import models


class m_team(models.Model):
    id = models.AutoField(primary_key=True, null=False, editable=False, auto_created=True)
    team_name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    coach = models.CharField(max_length=300, null=True, blank=False, default=None)
    captain = models.CharField(max_length=300, null=True, blank=False, default=None)
    stadium = models.CharField(max_length=300, null=True, blank=False, default=None)
    location = models.CharField(max_length=300, null=True, blank=False, default=None)
    wins = models.IntegerField(null=False, blank=False, default=0)
    losses = models.IntegerField(null=False, blank=False, default=0)
    draws = models.IntegerField(null=False, blank=False, default=0)
    class Meta:
        # abstract = True
        app_label = 'matches'
    def __str__(self) -> (str):
        return self.team_name


class m_match(models.Model):
    id = models.AutoField(primary_key=True, null=False, editable=False, auto_created=True)
    team1 = models.ForeignKey(to=m_team, on_delete=models.SET_NULL, null=True, related_name="match_team1", default=None)
    team2 = models.ForeignKey(to=m_team, on_delete=models.SET_NULL, null=True, related_name="match_team2", default=None)
    score1 = models.IntegerField(null=False, blank=False, default=0)
    score2 = models.IntegerField(null=False, blank=False, default=0)
    start_time_tz = models.DateTimeField(null=True, blank=False, default=None)
    end_time_tz = models.DateTimeField(null=True, blank=False, default=None)
    class Meta:
        # abstract = True
        app_label = 'matches'
    def __str__(self) -> (str):
        return self.team1 + " vs " + self.team1 