from django.db import models

class sendMail(models.Model):
    email = models.CharField(max_length=50)
    rss = models.CharField(max_length=50)