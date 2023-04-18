from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Player(models.Model):


    POINTGUARD = 'PG'
    SHOOTINGGUARD = 'SG'
    SMALLFORWARD = 'SF'
    POWERFORWARD = 'PF'
    CENTER = 'C'

    POSITION_CHOICES = [
        (POINTGUARD, 'Point Guard'),
        (SHOOTINGGUARD, 'Shooting Guard'),
        (SMALLFORWARD, 'Small Forward'),
        (POWERFORWARD, 'Power Forward'),
        (CENTER, 'Center')
        
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, default = '')
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
    
    def data_score(self):
        
        stats = {
            'points_per_game': {
                (0,2): 0,
                (2,5): 0.2,
                (5,8): 0.3,
                (8,12): 0.45,
                (12,16): 0.55,
                (16,20): 0.8,
                (20,25): 0.9,
                (25,float('inf')): 1
            },
            'rebounds_per_game':{
                (0,4):0,
                (4,6):0.3,
                (6,8):0.5,
                (8,11):0.75,
                (11,13):0.95,
                (13,float('inf')):1
            },
            'assists_per_game':{
                (0,2):0,
                (2,4):0.6,
                (4,6):1,
                (6,8):1.4,
                (8,10):1.7,
                (10,12):1.95,
                (12,float('inf')):2
            },
            'steals_per_game':{
                (0,1):0,
                (1,2):0.2,
                (2,4):0.5,
                (4,6):0.8,
                (6,9):0.95,
                (9,float('inf')):1
            },
            'blocks_per_game':{
                (0,1):0,
                (1,2):0.4,
                (2,4):0.6,
                (4,7):0.85,
                (7,10):0.95,
                (10,float('inf')):1
            },
            'fieldgoals_per_game':{
                (0,1): 0,
                (1,3): 0.1,
                (3,5): 0.25,
                (5,7): 0.5,
                (7,10): 0.75,
                (10,15): 0.9,
                (15,20): 0.95,
                (20,float('inf')): 1
            },
            'three_point_field_goal_percentage':{
                (0,10):0,
                (10,15):0.1,
                (15,20):0.2,
                (20,25):0.3,
                (25,30):0.4,
                (30,35):0.55,
                (35,45):0.65,
                (45,55):0.75,
                (55,70):0.85,
                (70,85):0.95,
                (85,100):1
            },
            'free_throw_percentage':{
                (0,30):0,
                (30,40):0.1,
                (40,50):0.2,
                (50,60):0.35,
                (60,70):0.5,
                (70,80):0.75,
                (80,90):0.9,
                (90,95):0.95,
                (95,100):1
            }
        }

        score = 0
        for stat, ranges in stats.items():
            stat_value = getattr(self, stat)
            for r in ranges:
                if r[0] <= stat_value <= r[1]:
                    score+=ranges[r]
                    break
        return score


class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default='01-01-2000 00:00:00')
    description = models.TextField(null=True)

    def __str__(self):
        return self.title



    

