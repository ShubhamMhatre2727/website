# Generated by Django 3.2.7 on 2021-09-11 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gym_workout_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym_workout',
            name='thumbnail',
        ),
    ]
