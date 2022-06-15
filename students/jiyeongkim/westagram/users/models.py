from django.db import models

class User(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    email           = models.CharField(max_length=45, unique=True)
    password        = models.CharField(max_length=200)
    line            = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'users'