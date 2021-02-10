from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length=200)

