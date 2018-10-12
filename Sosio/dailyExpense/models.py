from django.db import models

class registerdb(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)
    phone_no = models.IntegerField(default=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

