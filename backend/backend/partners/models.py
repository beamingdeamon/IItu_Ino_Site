from django.db import models

class Partner( models.Model):
    imgSource = models.CharField(max_length=60)
    text = models.CharField(max_length=60)