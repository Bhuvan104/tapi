from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.EmailField(max_length = 150)
    password = models.CharField(max_length=30)
    cpassword = models.CharField(max_length=30)
