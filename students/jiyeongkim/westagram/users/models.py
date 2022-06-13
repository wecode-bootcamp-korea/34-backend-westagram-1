from django.db import models

# Create your models here.
class User(models.Model):
    name            = models.TextField(max_length=45)
    email           = models.CharField(max_length=45, unique=True)
    Password        = models.CharField(max_length=45, null=False)
    line            = models.IntegerField(unique=True)

    class Meta:
        db_table = 'user'


