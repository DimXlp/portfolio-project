"""
 This file was written by me.
 It creates the Job app.
"""

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
