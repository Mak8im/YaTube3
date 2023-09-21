from django.db import models


class Person(models.Model):
    fio = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=30, default="")
    about = models.CharField(max_length=250, default="")

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo_url = models.URLField()
    description = models.CharField(max_length=250)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
