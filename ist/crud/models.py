from django.db import models


class Student(models.Model):
    Sid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age= models.PositiveIntegerField()
    email = models.EmailField()

# Create your models here.
