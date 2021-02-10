from django.db import models


class Apps(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=200)
