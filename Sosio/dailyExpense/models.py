import email

from django.db import models

class registerdb(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_no = models.IntegerField(default=10, unique=True)
    email = models.EmailField(max_length=25, primary_key=True)
    password = models.CharField(max_length=10)


class Userdetails(models.Model):

    phone_no = models.IntegerField(default=10)
    date = models.DateField()
    list = models.CharField(max_length=10)
    expense = models.IntegerField()

class friendsList(models.Model):
    phone_no = models.IntegerField(default=10)
    friend = models.CharField(max_length=20)
