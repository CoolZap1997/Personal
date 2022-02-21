from django.db import models

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Others',),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(min_length=8, max_length=100)
    country_code = models.CharField(min_length=2, max_length=4)
    phone = models.BigIntegerField(max_length=10)


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.CharField(max_length=30, unique=True)
