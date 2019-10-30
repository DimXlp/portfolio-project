"""
 This file was written by me.
 It creates the Blog app.
"""

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    """ added so we can see the blog titles
        in the admin page and not the Blog object """
    def __str__(self):
        return self.title

    # added, shows only the 100 first characters of the body
    def summary(self):
        return self.body[:100]+"..."

    # added, removes the time, shows only the date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
