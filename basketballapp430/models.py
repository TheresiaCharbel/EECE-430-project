from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Player(models.Model):


    POINTGUARD = 'PG'
    SHOOTINGGUARD = 'SG'
    SMALLFORWARD = 'SF'
    POWERFORWARD = 'PF'
    CENTER = 'C'

    POSITION_CHOICES = [
        (POINTGUARD, 'PG'),
        (SHOOTINGGUARD, 'SG'),
        (SMALLFORWARD, 'SF'),
        (POWERFORWARD, 'PF'),
        (CENTER, 'C')
        
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = CountryField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    games_played = models.IntegerField(default=0)
    points_per_game = models.FloatField(default=0)
    rebounds_per_game = models.FloatField(default=0)
    assists_per_game = models.FloatField(default=0)
    steals_per_game = models.FloatField(default=0)
    blocks_per_game = models.FloatField(default=0)
    fieldgoals_per_game = models.FloatField(default=0)
    three_point_field_goal_percentage = models.FloatField(default=0)
    free_throw_percentage = models.FloatField(default=0)

    def __str__(self):
        return self.name


    

