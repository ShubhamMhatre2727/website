from django.db import models

# Create your models here.
class Gym_Workout(models.Model):
    title = models.CharField(max_length=120)
    video = models.FileField(upload_to='gym_workout')
    thumbnail = models.FileField(upload_to='gym_workout')

    def __str__(self):
        return self.title
    