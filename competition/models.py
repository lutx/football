from django.db import models


class LeagueType(models.Model):
    name1 = models.CharField(max_length=100)


    def __str__(self):
        return self.name1

class Team(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Match(models.Model):
    host = models.ForeignKey(Team, related_name='matches_as_host')
    guest = models.ForeignKey(Team, related_name='MatchGuest')
    date = models.DateField()
    hostGoals = models.IntegerField()
    guestGoals = models.IntegerField()

    def __str__(self):
            return "{}-{}".format(self.host, self.guest)

class Kolejka(models.Model):
    name = models.ForeignKey(LeagueType)
    match = models.ForeignKey(Match)

    def __str__(self):
        return "{}-{}".format(self.name, self.match)



class Table (models.Model):
    name = models.ForeignKey(Team)
    name1 = models.ForeignKey(LeagueType)
    points = models.IntegerField

class Player(models.Model):
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    age = models.IntegerField()
    team=models.ForeignKey(Team)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.sname, self.team)

class MatchFacts (models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    incydent = models.CharField(max_length=300)






