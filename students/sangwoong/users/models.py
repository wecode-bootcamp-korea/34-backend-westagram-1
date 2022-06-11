from django.db import models

# Create your models here.
class User(models.Model) :
  last_name     = models.CharField(max_length=16) 
  first_name    = models.CharField(max_length=45)
  email         = models.EmailField(max_length=254, unique=True)
  account       = models.CharField(max_length=45)
  password      = models.CharField(max_length=128)
  phone_number  = models.CharField(max_length=32)
  date_of_birth = models.DateField()

  class Meta :
    db_table = "users"