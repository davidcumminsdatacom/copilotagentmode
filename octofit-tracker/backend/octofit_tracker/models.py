from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    user_id = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user_id = models.CharField(max_length=255)
    score = models.IntegerField()

class Workout(models.Model):
    workout_name = models.CharField(max_length=255)
    reps = models.IntegerField()
